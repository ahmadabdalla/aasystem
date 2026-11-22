#!/usr/bin/env node
// Capture Design Judge alignment measurements for one page state.
//
//   node capture.mjs <url> <outDir> [--widths 1440,390] [--schemes light,dark]
//                    [--prep prep.mjs] [--tag name] [--settle 1500]
//
// Needs the `playwright` package: installed where Node can resolve it, or in PLAYWRIGHT_DIR
// (a folder whose node_modules holds it). CHROMIUM_PATH selects an existing Chromium build.
// prep.mjs default-exports `async (page) => {}` to sign in, switch an in-app theme, or open a menu,
// dialog or tab first. An inner scroller at least half the viewport tall is shown in full (up to 20000px
// of overflow); smaller scrollers keep only their visible part.
// Writes <slug>.png (2x, full page, guides and misses drawn) and <slug>.json for every width
// and scheme, and prints each container's lines and misses.
// Exit codes: 0 no misses, 1 misses found, 2 invalid arguments, 3 capture failed,
// 4 nothing measured (no container had an edge line).
import { createRequire } from "node:module";
import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const USAGE = "usage: node capture.mjs <url> <outDir> [--widths 1440,390] [--schemes light,dark] [--prep file] [--tag name] [--settle ms]";
const KNOWN = new Set(["widths", "schemes", "prep", "tag", "settle"]);
const fail = (message) => { console.error(`${message}\n${USAGE}`); process.exit(2); };
const crash = (error) => { console.error(error); process.exit(3); };
process.on("uncaughtException", crash);
process.on("unhandledRejection", crash);

const [url, outDir, ...rest] = process.argv.slice(2);
if (!url || !outDir) fail("missing <url> or <outDir>");
const flags = {};
for (let i = 0; i < rest.length; i += 2) {
  const name = rest[i]?.replace(/^--/, "");
  if (!rest[i]?.startsWith("--") || !KNOWN.has(name) || rest[i + 1] === undefined) fail(`unknown or incomplete option: ${rest[i]}`);
  flags[name] = rest[i + 1];
}
const widths = (flags.widths ?? "1440,390").split(",").map(Number);
if (widths.some((w) => !Number.isInteger(w) || w < 200)) fail(`invalid --widths: ${flags.widths}`);
const schemes = (flags.schemes ?? "light").split(",");
if (schemes.some((s) => !["light", "dark"].includes(s))) fail(`invalid --schemes: ${flags.schemes}`);
const settle = Number(flags.settle ?? 1500);
if (!Number.isInteger(settle) || settle < 0) fail(`invalid --settle: ${flags.settle}`);

const loadPlaywright = async () => {
  if (process.env.PLAYWRIGHT_DIR) return createRequire(join(resolve(process.env.PLAYWRIGHT_DIR), "package.json"))("playwright");
  return import("playwright");
};
const { chromium } = await loadPlaywright();
const probe = readFileSync(join(dirname(fileURLToPath(import.meta.url)), "measure.js"), "utf8");
const prep = flags.prep ? (await import(pathToFileURL(resolve(flags.prep)).href)).default : null;

// Names come from the page actually measured, after any prep navigation.
const slugOf = (address) => {
  const target = new URL(address);
  const part = target.protocol === "file:" ? target.pathname.split("/").pop() : target.pathname + target.search;
  return part.replace(/\W+/g, "-").slice(0, 60).replace(/^-|-$/g, "") || "root";
};
mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH || undefined });
let misses = 0;
let measured = 0;
let unmeasured = 0;
// Grow the viewport until the tallest page-sized inner scroller shows all its content.
const innerOverflow = () => Math.max(0, ...[...document.querySelectorAll("*")].map((el) =>
  el !== document.scrollingElement && el !== document.body && /auto|scroll/.test(getComputedStyle(el).overflowY) &&
  el.clientHeight >= innerHeight / 2 ? el.scrollHeight - el.clientHeight : 0));
try {
  for (const width of widths) {
    const shots = [];
    for (const scheme of schemes) {
      const context = await browser.newContext({ viewport: { width, height: 1000 }, deviceScaleFactor: 2, colorScheme: scheme, bypassCSP: true });
      const page = await context.newPage();
      await page.goto(url, { waitUntil: "load" });
      await page.waitForTimeout(settle);
      if (prep) await prep(page);
      await page.mouse.move(0, 0); // no hover state from prep
      const overflow = await page.evaluate(innerOverflow);
      if (overflow > 0) {
        await page.setViewportSize({ width, height: 1000 + Math.min(overflow, 20000) });
        await page.waitForTimeout(Math.min(settle, 500));
      }
      await page.evaluate(probe);
      const containers = await page.evaluate(() => window.__designJudge.measure());
      const slug = [slugOf(page.url()), width, scheme, flags.tag].filter(Boolean).join("-");
      writeFileSync(join(outDir, `${slug}.json`), JSON.stringify({ url: page.url(), width, scheme, tag: flags.tag ?? null, containers }, null, 1));
      const shot = await page.screenshot({ path: join(outDir, `${slug}.png`), fullPage: true });
      await context.close();
      if (shots.some((s) => s.equals(shot))) console.warn(`warning: the ${scheme} capture at ${width}px is identical to another scheme; switch an in-app theme in prep`);
      shots.push(shot);

      console.log(`\n# ${slug}`);
      for (const c of containers) {
        if (c.unmeasured) unmeasured += 1;
        else measured += 1;
        const lines = Object.entries(c.lines).filter(([, v]) => v !== undefined).map(([key, v]) => `${key} ${v}px`);
        console.log(`## ${c.container} ${c.direction}  ${c.unmeasured ? "UNMEASURED (no edge line)" : lines.join("  ")}`);
        for (const m of c.misses) console.log(`   MISS ${m.edges.join("+")} y${m.y}: ${m.px}px, expected ${m.expected}px (${m.delta > 0 ? "+" : ""}${m.delta}px)${m.count > 1 ? ` x${m.count}` : ""}  ${m.item}`);
        misses += c.misses.length;
      }
      console.log(`capture: ${join(outDir, `${slug}.png`)}`);
    }
  }
} finally {
  await browser.close();
}
console.log(`\n${misses} misses; ${measured} containers measured, ${unmeasured} unmeasured`);
process.exitCode = misses ? 1 : measured ? 0 : 4;
