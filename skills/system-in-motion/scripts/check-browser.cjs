#!/usr/bin/env node
'use strict';
// Optional read-only browser verification. Requires Playwright in the caller's
// environment; the generated HTML itself has no runtime dependencies.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const assert = require('node:assert/strict');
const { chromium } = require('playwright');
const verifyBusinessGeometry = require('./business-geometry.cjs');

const args = process.argv.slice(2);
if (!args[0] || (args.length > 1 && (args[1] !== '--screenshots' || !args[2])) || args.length > 3) {
  console.error('Usage: node check-browser.cjs FILE [--screenshots DIR]');
  process.exit(2);
}
const file = path.resolve(args[0]);
if (!fs.statSync(file).isFile()) throw new Error(`Not a file: ${file}`);
const screenshotDir = args[2] && path.resolve(args[2]);
if (screenshotDir) fs.mkdirSync(screenshotDir, { recursive: true });
const close = (a, b, message, tolerance = 0.06) =>
  assert(Math.abs(a - b) <= tolerance, `${message}: ${a} versus ${b}`);

async function state(page) {
  return page.evaluate(() => window.systemInMotion.getState());
}
async function settleGeometry(page) {
  await page.clock.runFor(80);
  await page.waitForFunction(
    () => document.getElementById('diagram').dataset.geometryReady === 'true',
  );
  await page.evaluate(() => document.fonts.ready);
}
async function verifyTechnicalGeometry(page) {
  return page.evaluate(() => {
    const model = window.systemInMotion.getModel(),
      diagram = document.getElementById('diagram');
    const base = diagram.getBoundingClientRect();
    const rect = (element) => {
      const r = element.getBoundingClientRect();
      return {
        left: r.left - base.left,
        top: r.top - base.top,
        right: r.right - base.left,
        bottom: r.bottom - base.top,
      };
    };
    const nodes = new Map(
      [...document.querySelectorAll('[data-component]')].map((element) => [
        element.dataset.component,
        {
          icon: rect(element.querySelector('svg')),
          caption: rect(element.querySelector('.em-node-caption')),
        },
      ]),
    );
    const headings = [...document.querySelectorAll('.lane-heading > *')]
      .flatMap((element) => {
        const range = document.createRange();
        range.selectNodeContents(element);
        return [...range.getClientRects()]
          .filter((r) => r.width && r.height)
          .map((r) => ({
            left: r.left - base.left,
            top: r.top - base.top,
            right: r.right - base.left,
            bottom: r.bottom - base.top,
          }));
      })
      .concat([...document.querySelectorAll('.em-cloud-label')].map(rect));
    const issues = [],
      paths = [...document.querySelectorAll('path.edge')];
    if (window.systemInMotion.getState().routeErrors.length)
      issues.push(`Unrouted exchanges: ${window.systemInMotion.getState().routeErrors.join(', ')}`);
    if (!nodes.size || nodes.size !== model.components.length)
      issues.push(`Expected ${model.components.length} node captions; found ${nodes.size}`);
    if (paths.length !== model.edges.length)
      issues.push(`Expected ${model.edges.length} paths; found ${paths.length}`);
    const annotations = paths.filter((p) => p.querySelector('title')?.textContent.trim());
    if (annotations.length !== model.edges.length)
      issues.push(`Expected ${model.edges.length} exchange title annotations; found ${annotations.length}`);
    const docked = (p, r) =>
      Math.min(
        ...[
          p.x >= r.left - 1 && p.x <= r.right + 1 ? Math.abs(p.y - r.top) : Infinity,
          p.x >= r.left - 1 && p.x <= r.right + 1 ? Math.abs(p.y - r.bottom) : Infinity,
          p.y >= r.top - 1 && p.y <= r.bottom + 1 ? Math.abs(p.x - r.left) : Infinity,
          p.y >= r.top - 1 && p.y <= r.bottom + 1 ? Math.abs(p.x - r.right) : Infinity,
        ],
      ) <= 1;
    const crosses = (a, b, r) =>
      Math.abs(a.x - b.x) < 0.1
        ? a.x > r.left + 0.5 &&
          a.x < r.right - 0.5 &&
          Math.max(a.y, b.y) > r.top + 0.5 &&
          Math.min(a.y, b.y) < r.bottom - 0.5
        : a.y > r.top + 0.5 &&
          a.y < r.bottom - 0.5 &&
          Math.max(a.x, b.x) > r.left + 0.5 &&
          Math.min(a.x, b.x) < r.right - 0.5;
    for (const edge of model.edges) {
      const element = paths.find((p) => p.dataset.edge === edge.id);
      if (!element) continue;
      const values = element
          .getAttribute('d')
          .match(/-?\d+(?:\.\d+)?/g)
          .map(Number),
        points = [];
      for (let i = 0; i < values.length; i += 2) points.push({ x: values[i], y: values[i + 1] });
      if (points.length < 2) {
        issues.push(`${edge.id}: no route`);
        continue;
      }
      if (!Object.values(nodes.get(edge.from)).some((r) => docked(points[0], r)))
        issues.push(`${edge.id}: source not docked`);
      if (!Object.values(nodes.get(edge.to)).some((r) => docked(points.at(-1), r)))
        issues.push(`${edge.id}: target not docked`);
      if (element.dataset.kind !== edge.kind) issues.push(`${edge.id}: kind lost`);
      if (edge.kind === 'observe' && element.getAttribute('marker-end') !== 'none')
        issues.push(`${edge.id}: observation has a calling arrow`);
      if (edge.kind !== 'observe' && !element.getAttribute('marker-end').startsWith('url('))
        issues.push(`${edge.id}: direction marker missing`);
      // A wide flex heading's empty area must not force perimeter detours.
      // Compare the drawn path with clear, short orthogonal corridors using the
      // same measured icon/caption/text obstacles and endpoint stub directions.
      const obstacles = [...nodes.values()]
        .flatMap((g) => Object.values(g))
        .concat(headings)
        .map((r) => ({
          left: r.left - 7,
          top: r.top - 7,
          right: r.right + 7,
          bottom: r.bottom + 7,
        }));
      const start = points[0],
        end = points.at(-1),
        next = points[1],
        prior = points.at(-2);
      const stub = (p, t) => ({
        x: p.x + Math.sign(t.x - p.x) * Math.min(10, Math.abs(t.x - p.x)),
        y: p.y + Math.sign(t.y - p.y) * Math.min(10, Math.abs(t.y - p.y)),
      });
      const a = stub(start, next),
        b = stub(end, prior),
        candidates = [];
      const xs = [a.x, b.x, ...obstacles.flatMap((r) => [r.left, r.right])],
        ys = [a.y, b.y, ...obstacles.flatMap((r) => [r.top, r.bottom])];
      for (const x of xs) candidates.push([a, { x, y: a.y }, { x, y: b.y }, b]);
      for (const y of ys) candidates.push([a, { x: a.x, y }, { x: b.x, y }, b]);
      const length = (ps) =>
        ps.slice(1).reduce((n, p, i) => n + Math.abs(p.x - ps[i].x) + Math.abs(p.y - ps[i].y), 0);
      const clear = candidates.filter((ps) =>
        ps.slice(1).every((p, i) => !obstacles.some((r) => crosses(ps[i], p, r))),
      );
      if (clear.length && length(points) > Math.min(...clear.map(length)) + 20 + 72)
        issues.push(`${edge.id}: avoidable perimeter detour around empty heading space`);
      for (let i = 1; i < points.length; i++) {
        const a = points[i - 1],
          b = points[i];
        if (Math.abs(a.x - b.x) > 0.1 && Math.abs(a.y - b.y) > 0.1)
          issues.push(`${edge.id}: nonorthogonal segment`);
        for (const [id, geometry] of nodes)
          if (Object.values(geometry).some((r) => crosses(a, b, r)))
            issues.push(`${edge.id}: crosses node/caption ${id}`);
        for (const r of headings)
          if (crosses(a, b, r)) issues.push(`${edge.id}: crosses lane heading`);
        for (const p of [a, b])
          if (p.x < -0.5 || p.x > base.width + 0.5 || p.y < -0.5 || p.y > base.height + 0.5)
            issues.push(`${edge.id}: outside diagram`);
      }
    }
    const svg = document.getElementById('connectors');
    if (Math.abs(svg.viewBox.baseVal.width - svg.getBoundingClientRect().width) > 1)
      issues.push('Diagram was scaled instead of reflowed');
    if (document.documentElement.scrollWidth > innerWidth + 1)
      issues.push(`Horizontal overflow: ${document.documentElement.scrollWidth} > ${innerWidth}`);
    for (const element of document.querySelectorAll(
      '.em-map-node,.lane-heading,.em-window,.em-engine',
    )) {
      const r = element.getBoundingClientRect();
      if (r.left < -0.5 || r.right > innerWidth + 0.5)
        issues.push(`Offscreen block: ${element.className}`);
      if (element.scrollWidth > element.clientWidth + 1)
        issues.push(`Block content overflow: ${element.className}`);
    }
    return { issues: [...new Set(issues)], nodeCount: nodes.size, edgeCount: paths.length, annotationCount: annotations.length };
  });
}

(async () => {
  const browser = await chromium.launch(
    { ...(process.env.PLAYWRIGHT_CHANNEL ? {channel:process.env.PLAYWRIGHT_CHANNEL} : {}),
      ...(process.env.BROWSER_EXECUTABLE_PATH ? {executablePath:process.env.BROWSER_EXECUTABLE_PATH} : {}) },
  );
  const context = await browser.newContext({
    viewport: { width: 1280, height: 800 },
    colorScheme: 'light',
  });
  const page = await context.newPage(),
    errors = [],
    remote = [];
  page.on('pageerror', (error) => errors.push(error.message));
  page.on('request', (request) => {
    if (!/^(file|data|about):/.test(request.url())) remote.push(request.url());
  });
  try {
    const epoch = new Date('2026-01-01T00:00:00Z');
    await page.clock.install({ time: epoch });
    await page.goto(pathToFileURL(file).href);
    await page.clock.pauseAt(new Date(epoch.getTime() + 1000));
    const model = await page.evaluate(() => window.systemInMotion.getModel());
    assert((await state(page)).playing, 'Playback must start automatically');
    await page.click('#replay');
    await page.clock.runFor(600);
    assert((await state(page)).elapsed > 0.4, 'Autoplay did not advance');
    const business = model.presentation?.profile === 'business-workflow';
    assert.equal((await state(page)).view, business ? 'architecture' : 'experience', 'Incorrect profile opening view');
    const verifyGeometry = business ? verifyBusinessGeometry : verifyTechnicalGeometry;
    const showMap = async () => {
      if ((await state(page)).view !== 'architecture') {
        const toggle = page.getByRole('button', { name: business ? 'Business map' : 'Architecture', exact: true });
        assert.equal(await toggle.getAttribute('aria-pressed'), null, 'View toggle exposed a pressed state');
        await toggle.click();
      }
    };
    const showExperience = async () => {
      if ((await state(page)).view !== 'experience') await page.getByRole('button', {name:'Experience',exact:true}).click();
    };
    await showMap();
    await settleGeometry(page);
    const beforeView = await state(page);
    await showExperience();
    close((await state(page)).elapsed, beforeView.elapsed, 'Switching views reset scene time');
    const beforeGap = await state(page);
    await page.clock.fastForward(Math.ceil((beforeGap.total + 1) * 1000));
    const afterGap = await state(page);
    assert.equal(afterGap.index, beforeGap.index, 'Long frame gap skipped the current scene');
    assert(afterGap.playing && !afterGap.complete, 'Long frame gap stopped playback');
    assert(
      afterGap.elapsed <= beforeGap.elapsed + 0.25,
      'Long frame gap advanced playback by more than 250 ms',
    );
    await showMap();
    await settleGeometry(page);
    await page.click('#play');
    const paused = await state(page);
    const packetBefore = await page
      .locator('.packet,.em-move')
      .evaluateAll((items) =>
        items.map((e) => [
          e.getAttribute('cx'),
          e.getAttribute('cy'),
          e.style.transform,
          e.style.opacity,
        ]),
      );
    await page.clock.runFor(1200);
    close((await state(page)).elapsed, paused.elapsed, 'Pause changed scene time', 0.001);
    assert.deepEqual(
      await page
        .locator('.packet,.em-move')
        .evaluateAll((items) =>
          items.map((e) => [
            e.getAttribute('cx'),
            e.getAttribute('cy'),
            e.style.transform,
            e.style.opacity,
          ]),
        ),
      packetBefore,
      'Pause did not freeze packet movement',
    );
    await page.click('#play');
    await page.clock.runFor(300);
    assert((await state(page)).elapsed > paused.elapsed + 0.2, 'Resume did not advance');
    if (
      model.scenes[0].activeEdges.some(
        (id) => model.edges.find((edge) => edge.id === id).kind !== 'observe',
      )
    ) {
      assert.notDeepEqual(
        await page
          .locator('.packet,.em-move')
          .evaluateAll((items) =>
            items.map((e) => [
              e.getAttribute('cx'),
              e.getAttribute('cy'),
              e.style.transform,
              e.style.opacity,
            ]),
          ),
        packetBefore,
        'Resumed exchange tokens did not move',
      );
    }
    if (model.scenes.length > 1) {
      await showExperience();
      await page.click('#replay');
      await page.click('#play');
      const entryOpacity = () => page
        .locator('#stage .em-move:not([data-motion="travel"])')
        .evaluateAll((items) => items.map((element) => Number(getComputedStyle(element).opacity)));
      assert((await entryOpacity()).every((opacity) => opacity === 1), 'Pause left current scene text faded');
      await page.click('#play');
      await page.clock.runFor(80);
      assert((await entryOpacity()).every((opacity) => opacity === 1), 'Resume hid already revealed current content');
      const resumed = await state(page);
      await page.clock.runFor(Math.ceil((model.scenes[0].duration - resumed.elapsed) * 1000) + 40);
      assert.equal((await state(page)).index, 1, 'Resume did not reach the next scene automatically');
      const entering = await entryOpacity();
      if (entering.length) {
        assert(entering.some((opacity) => opacity < 0.95), 'Automatic scene entry stayed fully revealed after Pause/Resume');
        await page.clock.runFor(1600);
        assert.equal((await state(page)).index, 1, 'Entry check skipped the new scene');
        assert.equal((await entryOpacity())[0], 1, 'New scene entry never became fully readable');
      }
    }
    await page.click('#replay');
    close((await state(page)).elapsed, 0, 'Replay did not reset', 0.001);
    assert.equal((await state(page)).index, 0, 'Replay did not return to first scene');
    await page.click('#play');

    // Rebuilding the hidden experience during graph measurement must not leave
    // its paused traveling object at a zero-width position when revealed again.
    const processingIndex = model.scenes.findIndex(
      (scene) => scene.experience.layout === 'pipeline' || scene.experience.layout === 'dispatch',
    );
    if (processingIndex >= 0) {
      await page.click(`.em-step[data-scene="${processingIndex}"]`);
      await showExperience();
      await page.click('#play');
      await page.clock.runFor(900);
      await page.click('#play');
      const held = await state(page);
      const objectPosition = () =>
        page
          .locator('#stage .em-envelope')
          .evaluate((e) => ({ x: e.getBoundingClientRect().x, transform: e.style.transform }));
      const beforeRoundtrip = await objectPosition();
      await showMap();
      await settleGeometry(page);
      await showExperience();
      const afterRoundtrip = await objectPosition();
      close(
        afterRoundtrip.x,
        beforeRoundtrip.x,
        'Paused traveling object jumped after view roundtrip',
        0.5,
      );
      close((await state(page)).elapsed, held.elapsed, 'View roundtrip changed paused time', 0.001);
      assert.equal((await state(page)).index, held.index, 'View roundtrip changed scene');
      assert(!(await state(page)).playing, 'View roundtrip resumed playback');
      await showMap();
      await settleGeometry(page);
    }

    // Label updates are observable DOM changes; a stable value should not be
    // replaced on every animation frame (particularly disruptive to VoiceOver).
    await page.click('#replay');
    await page.evaluate(() => {
      window.controlLabelMutations = 0;
      window.controlLabelObserver = new MutationObserver((records) => { window.controlLabelMutations += records.length; });
      for (const id of ['play','clock','autostatus'])
        window.controlLabelObserver.observe(document.getElementById(id), {subtree:true,childList:true,characterData:true});
    });
    await page.clock.runFor(500);
    assert.equal(await page.evaluate(() => window.controlLabelMutations), 0, 'Unchanged control labels were replaced during playback');
    await page.evaluate(() => window.controlLabelObserver.disconnect());
    await page.click('#play');
    await page.click('.em-step[data-scene="0"]');
    assert(await page.locator('#back').isDisabled(), 'Back should be disabled at the first scene');
    if (model.scenes.length > 1) {
      await page.click('#next');
      assert.equal((await state(page)).index, 1, 'Next did not advance');
      await page.click('#back');
      assert.equal((await state(page)).index, 0, 'Back did not return');
    }
    if (business) {
      await showMap();
      for (const item of model.components.filter((node) => node.scene)) {
        const sceneIndex = model.scenes.findIndex((scene) => scene.id === item.scene);
        const node = page.locator(`.business-node[data-component="${item.id}"]`);
        for (const key of ['Enter','Space']) {
          await node.focus();
          await page.keyboard.press(key);
          assert.equal((await state(page)).index, sceneIndex, `${key} did not select ${item.id}`);
          assert(!(await state(page)).playing, 'Keyboard selection resumed paused playback');
          assert.equal(await node.evaluate((element) => document.activeElement === element), true, 'Node lost keyboard focus');
          assert(await node.locator('.node-shape').evaluate((shape) => parseFloat(getComputedStyle(shape).strokeWidth) >= 3), 'Node focus has no visible outline');
        }
        await node.click();
        assert.equal((await state(page)).index, sceneIndex, 'Node click did not select its canonical scene');
      }
      const phasedIndex = model.scenes.findIndex((scene) => scene.phases?.length > 1);
      if (phasedIndex >= 0) {
        const phased = model.scenes[phasedIndex], phaseMs = phased.duration * 1000 / phased.phases.length;
        await page.click(`.em-step[data-scene="${phasedIndex}"]`);
        await page.click('#play');
        for(let phase=0;phase<phased.phases.length;phase++) {
          await page.clock.runFor(phase ? phaseMs : phaseMs / 2);
          assert.equal((await state(page)).activePhase, phase, 'Narrative phase order changed');
          const visible = await page.locator('.packet').evaluateAll((items) => items
            .filter((packet) => getComputedStyle(packet).display !== 'none')
            .map((packet) => packet.dataset.packetEdge));
          const expected = phased.phases[phase].edges.filter((id) => model.edges.find((edge) => edge.id === id).kind !== 'prerequisite');
          assert.deepEqual(visible.sort(), expected.sort(), 'Only the active phase may travel');
        }
        await page.click('#play');
      }
    }

    let count = 0;
    for (const theme of ['light', 'dark'])
      for (const { width, height } of [{ width: 1280, height: 800 }, { width: 1440, height: 900 }]) {
        await page.setViewportSize({ width, height });
        await page.emulateMedia({ colorScheme: theme });
        await page.click('#replay');
        await page.click('#play');
        await settleGeometry(page);
        for (let i = 0; i < model.scenes.length; i++) {
          await page.click(`.em-step[data-scene="${i}"]`);
          await settleGeometry(page);
          assert.equal((await state(page)).index, i, 'Next did not select expected scene');
          const geometry = await verifyGeometry(page);
          assert.deepEqual(
            geometry.issues,
            [],
            `${theme}/${width}/scene ${i + 1}: ${geometry.issues.join('; ')}`,
          );
          assert.equal(await page.locator('#scene-title').textContent(), model.scenes[i].title);
          assert.equal(await page.locator('#next').isDisabled(), i === model.scenes.length - 1, 'Next disabled state disagrees with scene');
          if (business) {
            const dimensions = await page.locator('#state-strip').textContent();
            for (const dimension of model.stateDimensions) {
              assert(dimensions.includes(dimension.label), 'Missing model state dimension label');
              assert(dimensions.includes(model.scenes[i].states[dimension.id]), 'Missing scene state dimension value');
            }
            const movingPrerequisites = await page.locator('.packet').evaluateAll((packets) => {
              const edges = window.systemInMotion.getModel().edges;
              return packets.filter((packet) => edges.find((edge) => edge.id === packet.dataset.packetEdge)?.kind === 'prerequisite' &&
                getComputedStyle(packet).display !== 'none').length;
            });
            assert.equal(movingPrerequisites, 0, 'A prerequisite animated as an initiating call');
          }
          await showExperience();
          const surface = await page.evaluate(() => ({
            overflow: document.documentElement.scrollWidth > innerWidth + 1,
            title: document.querySelector('#stage h3').textContent,
            buttons: document.querySelectorAll('#surface button').length,
            layout: document.querySelector('#stage [data-layout]').dataset.layout,
          }));
          assert(!surface.overflow, `${theme}/${width}/experience scene ${i + 1} overflows`);
          assert.equal(surface.title, model.scenes[i].experience.title);
          assert.equal(surface.buttons, 0, 'Illustrative surface has live buttons');
          assert.equal(surface.layout, model.scenes[i].experience.layout);
          assert(!(await state(page)).playing, 'Paused scene selection resumed the clock');
          close((await state(page)).elapsed, 0, 'Reading paused content advanced simulation time', 0.001);
          const unreadable = await page.locator('#stage .em-move').evaluateAll((items) => items
            .filter((element) => parseFloat(getComputedStyle(element).opacity) < 0.99)
            .map((element) => element.textContent));
          assert.deepEqual(unreadable, [], 'Paused selection left explanatory content faded');
          const anchors = await page.evaluate(() => {
            const r = (s) => document.querySelector(s).getBoundingClientRect();
            return {
              header: r('.em-top').bottom,
              heading: r('.em-heading').top,
              window: r('.em-window').top,
              bottom: r('.em-window').bottom,
              controls: r('.em-controls').top,
              steps: r('.em-steps').top,
              controlsBottom: r('.em-controls').bottom,
              rail: r('.em-engine').width,
              toggles: document.querySelectorAll('#architecture-tab,#experience-tab').length,
            };
          });
          assert.equal(anchors.toggles, 1, 'Expected one view toggle');
          assert(
            anchors.header <= anchors.heading + 1 &&
              anchors.heading < anchors.window &&
              anchors.bottom <= anchors.controls + 1 &&
              anchors.controlsBottom <= anchors.steps + 1,
            'Presentation anchors moved out of order',
          );
          close(anchors.rail, 242, 'Backstage rail width', 1);
          assert.equal(await page.locator('body').evaluate((element) => getComputedStyle(element).backgroundColor), 'rgb(255, 255, 255)', 'OS dark preference changed the light palette');
          await page.click('#play');
          // Selecting while playing starts the scene's motion. A prior paused
          // selection deliberately revealed text and must not fade it on resume.
          await page.click(`.em-step[data-scene="${i}"]`);
          await page.clock.runFor(250);
          const movement = () =>
            page
              .locator('#stage .em-move')
              .evaluateAll((items) => items.map((e) => [e.style.transform, e.style.opacity]));
          const beforeMotion = await movement();
          const arrival = page.locator('#stage [data-motion=arrival]').first();
          const arrivalBefore = (await arrival.count())
            ? await arrival.evaluate((e) => e.getBoundingClientRect().x)
            : null;
          const travelingObject = page.locator('#stage .em-envelope');
          const travelBefore = (await travelingObject.count())
            ? await travelingObject.evaluate((e) => e.getBoundingClientRect().x)
            : null;
          await page.clock.runFor(400);
          if (travelBefore !== null)
            assert(
              (await travelingObject.evaluate((e) => e.getBoundingClientRect().x)) >
                travelBefore + 0.5,
              'Processing object did not travel toward the next stage',
            );
          if (arrivalBefore !== null)
            assert(
              (await arrival.evaluate((e) => e.getBoundingClientRect().x)) < arrivalBefore - 0.5,
              'Incoming object did not arrive into the scene',
            );
          if (beforeMotion.length)
            assert.notDeepEqual(
              await movement(),
              beforeMotion,
              'Scene objects did not move or reveal',
            );
          await page.click('#play');
          const heldMotion = await movement();
          await page.clock.runFor(300);
          assert.deepEqual(await movement(), heldMotion, 'Paused scene motion changed');
          if (model.scenes[i].experience.mode === 'explanation')
            assert(
              (await page.locator('#stage').textContent()).includes(business ? 'Workflow explanation' : 'System processing view'),
              'Explanatory processing is unlabeled',
            );
          if (screenshotDir)
            await page.screenshot({
              path: path.join(screenshotDir, `${theme}-${width}-experience-${i + 1}.png`),
              fullPage: true,
            });
          await showMap();
          await settleGeometry(page);
          if (screenshotDir)
            await page.screenshot({
              path: path.join(screenshotDir, `${theme}-${width}-scene-${i + 1}.png`),
              fullPage: true,
            });
          count++;
        }
      }
    await page.click('#evidence summary');
    await page.locator('#claim-select').selectOption(String(model.scenes.length - 1));
    const current = model.scenes.at(-1),
      evidence = await page.locator('#evidence-content').textContent();
    for (const id of current.evidence)
      assert(
        evidence.includes(model.sources.find((s) => s.id === id).location),
        `Missing source location ${id}`,
      );
    assert.equal(
      await page.locator('#evidence-content a').count(),
      0,
      'Evidence must be plain text',
    );
    await page.emulateMedia({ reducedMotion: 'reduce' });
    for (const view of ['architecture','experience']) {
      if (view === 'architecture') await showMap();
      else await showExperience();
      await page.click('#replay');
      const transitionIndex = model.scenes.length > 1 ? 1 : 0;
      const transitionMs = transitionIndex ? model.scenes[0].duration * 1000 + 200 : 300;
      await page.clock.runFor(transitionMs);
      assert.equal((await state(page)).index, transitionIndex, 'Automatic playback did not select expected scene');
      assert((await state(page)).elapsed > 0.1, 'Reduced motion disabled progression');
      assert.equal(await page.locator('#scene-title').textContent(), model.scenes[transitionIndex].title);
      if (view === 'experience')
        assert.equal(await page.locator('#stage h3').textContent(), model.scenes[transitionIndex].experience.title);
      assert.equal(
        await page.locator('.packet').evaluateAll((items) =>
          items.filter((element) => getComputedStyle(element).display !== 'none').length),
        0,
        'Reduced motion retained travel animation',
      );
      await page.clock.runFor(model.scenes.reduce((sum, scene) => sum + scene.duration * 1000, 0) + 200);
      const ended = await state(page);
      assert(ended.complete && !ended.playing, `${view}: journey did not finish cleanly`);
      assert(await page.locator('#play').isDisabled(), 'Completed playback button remained enabled');
      assert(await page.locator('#next').isDisabled(), 'Next remained enabled after completion');
      await page.clock.runFor(3000);
      assert.deepEqual(await state(page), ended, 'Completed journey continued changing');
      await page.locator('#replay').focus();
      await page.keyboard.press('Space');
      assert((await state(page)).playing && !(await state(page)).complete, 'Keyboard Replay did not restart');
      assert.equal((await state(page)).index, 0, 'Replay did not select first scene');
      await page.clock.runFor(150);
      assert((await state(page)).elapsed > 0.1, 'Restarted journey did not advance');
    }
    assert.deepEqual(errors, [], 'Browser runtime errors');
    assert.deepEqual(remote, [], 'Offline document attempted remote requests');
    console.log(
      `PASS: ${count} scene/theme/laptop-viewport cases (1280x800, 1440x900); ${business ? 'all business node/relationship caption coverage and clearance' : 'technical node caption coverage and exchange title annotations (no visible exchange captions)'}, measured endpoint docking, orthogonal routing, shape/caption/heading clearance and presentation anchors, laptop layout bounds, clock/view/pause/replay/completion, reduced motion, evidence text, and offline requests.`,
    );
    console.log(
      'This check verifies rendered geometry and playback; source truth, causal semantics, visual quality, and human acceptance still require review.',
    );
  } finally {
    await context.close();
    await browser.close();
  }
})().catch((error) => {
  console.error(error.stack || error.message);
  process.exitCode = 1;
});
