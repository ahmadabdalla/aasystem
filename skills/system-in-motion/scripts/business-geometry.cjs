'use strict';

// Profile adapter for the shared verifier. Measure in rendered CSS coordinates
// so SVG scaling, text wrapping and font metrics participate in the checks.
module.exports = async function verifyBusinessGeometry(page) {
  return page.evaluate(() => {
    const model = window.systemInMotion.getModel();
    const diagram = document.getElementById('diagram');
    const issues = [];
    const nodes = [...diagram.querySelectorAll('[data-component]')];
    const paths = [...diagram.querySelectorAll('path.edge')];
    const labels = [...diagram.querySelectorAll('[data-edge-label]')];
    const captions = [...diagram.querySelectorAll('.business-node-label')];
    const rect = (element) => {
      const r = element.getBoundingClientRect();
      return { left: r.left, right: r.right, top: r.top, bottom: r.bottom };
    };
    const overlaps = (a, b, gap = 0) =>
      a.left < b.right + gap && a.right > b.left - gap &&
      a.top < b.bottom + gap && a.bottom > b.top - gap;
    const contains = (r, p, padding = 0) =>
      p.x > r.left - padding && p.x < r.right + padding &&
      p.y > r.top - padding && p.y < r.bottom + padding;
    const crosses = (a, b, r, padding = 0) => Math.abs(a.x - b.x) < 0.1
      ? a.x > r.left - padding && a.x < r.right + padding &&
        Math.max(a.y, b.y) > r.top - padding && Math.min(a.y, b.y) < r.bottom + padding
      : a.y > r.top - padding && a.y < r.bottom + padding &&
        Math.max(a.x, b.x) > r.left - padding && Math.min(a.x, b.x) < r.right + padding;
    const toScreen = (element, point) =>
      new DOMPoint(point.x, point.y).matrixTransform(element.getScreenCTM());
    const shapeFor = (node) => node?.querySelector('.node-shape');
    const renderedPaths = paths.map((element) => {
      const values = (element.getAttribute('d').match(/-?\d+(?:\.\d+)?/g) || []).map(Number);
      const points = [];
      for (let i = 0; i < values.length; i += 2)
        points.push(toScreen(element, { x: values[i], y: values[i + 1] }));
      return { element, points, id: element.dataset.edge };
    });
    const pointShapeDistance = (point, shape) => {
      const length = shape.getTotalLength();
      let distance = Infinity;
      for (let offset = 0; offset <= length; offset += 0.6) {
        const p = toScreen(shape, shape.getPointAtLength(offset));
        distance = Math.min(distance, Math.hypot(p.x - point.x, p.y - point.y));
      }
      return distance;
    };
    const shapeOverlapsRect = (shape, box, padding = 0) => {
      if (!shape || !overlaps(rect(shape), box, padding)) return false;
      const inverse = shape.getScreenCTM().inverse();
      for (const x of [box.left - padding, (box.left + box.right) / 2, box.right + padding])
        for (const y of [box.top - padding, (box.top + box.bottom) / 2, box.bottom + padding])
          if (shape.isPointInFill(new DOMPoint(x, y).matrixTransform(inverse))) return true;
      const length = shape.getTotalLength();
      for (let offset = 0; offset <= length; offset += 0.6)
        if (contains(box, toScreen(shape, shape.getPointAtLength(offset)), padding)) return true;
      return false;
    };
    const headings = [...diagram.querySelectorAll('.lane-title,.lane-detail')].map(rect);
    if (!nodes.length || nodes.length !== model.components.length)
      issues.push(`Expected ${model.components.length} nodes; found ${nodes.length}`);
    if (!captions.length || captions.length !== model.components.length)
      issues.push(`Expected ${model.components.length} node captions; found ${captions.length}`);
    if (labels.length !== model.edges.length)
      issues.push(`Expected ${model.edges.length} relationship captions; found ${labels.length}`);
    if (paths.length !== model.edges.length)
      issues.push(`Expected ${model.edges.length} paths; found ${paths.length}`);
    if (window.systemInMotion.getState().routeErrors.length)
      issues.push('Unrouted business relationships');
    const bounds = rect(diagram);
    for (const node of nodes) {
      const item = model.components.find((c) => c.id === node.dataset.component);
      const shape = shapeFor(node);
      if (!item || !shape || typeof shape.getTotalLength !== 'function') {
        issues.push(`${node.dataset.component}: no resolved graphical shape`);
        continue;
      }
      const box = rect(shape), caption = node.querySelector('.business-node-label');
      if (!caption || !caption.textContent.trim())
        issues.push(`${item.id}: missing action/object caption`);
      if (box.left < bounds.left - 1 || box.right > bounds.right + 1 ||
          box.top < bounds.top - 1 || box.bottom > bounds.bottom + 1)
        issues.push(`${item.id}: outside diagram`);
      for (const text of node.querySelectorAll('.business-node-label,.business-node-detail')) {
        const r = rect(text);
        if (r.left < box.left + 3 || r.right > box.right - 3 ||
            r.top < box.top + 1 || r.bottom > box.bottom - 1)
          issues.push(`${item.id}: text does not fit shape`);
        if (text.classList.contains('business-node-label') &&
            parseFloat(getComputedStyle(text).fontSize) * Math.abs(text.getScreenCTM().a) < 12)
          issues.push(`${item.id}: action label smaller than 12 CSS px`);
      }
      if (node.dataset.status !== item.status) issues.push(`${item.id}: provenance status lost`);
      if (node.dataset.lane !== item.lane) issues.push(`${item.id}: performer lane lost`);
      const badge = node.querySelector('[data-step]');
      const expected = item.scene ? model.scenes.findIndex((scene) => scene.id === item.scene) + 1 : null;
      if ((badge ? Number(badge.dataset.step) : null) !== expected)
        issues.push(`${item.id}: badge disagrees with canonical scene`);
      if (item.status === 'planned' && getComputedStyle(shape).strokeDasharray === 'none')
        issues.push(`${item.id}: planned node became solid`);
    }
    for (const route of renderedPaths) {
      const edge = model.edges.find((e) => e.id === route.id);
      const { points, element } = route;
      if (!edge || points.length < 2) {
        issues.push(`${route.id}: missing route`);
        continue;
      }
      const from = shapeFor(nodes.find((n) => n.dataset.component === edge.from));
      const to = shapeFor(nodes.find((n) => n.dataset.component === edge.to));
      if (from && pointShapeDistance(points[0], from) > 2)
        issues.push(`${edge.id}: source not docked to visible shape`);
      if (to && pointShapeDistance(points.at(-1), to) > 2)
        issues.push(`${edge.id}: target not docked to visible shape`);
      if (element.dataset.kind !== edge.kind) issues.push(`${edge.id}: business meaning lost`);
      if (element.dataset.status !== edge.status) issues.push(`${edge.id}: provenance status lost`);
      if (!element.getAttribute('marker-end')?.startsWith('url('))
        issues.push(`${edge.id}: direction marker missing`);
      if (edge.status === 'planned' && getComputedStyle(element).strokeDasharray === 'none')
        issues.push(`${edge.id}: planned relationship became solid`);
      for (let i = 1; i < points.length; i++) {
        const a = points[i - 1], b = points[i];
        if (Math.abs(a.x - b.x) > 0.1 && Math.abs(a.y - b.y) > 0.1)
          issues.push(`${edge.id}: nonorthogonal segment`);
        for (const point of [a, b])
          if (!contains(bounds, point, 1)) issues.push(`${edge.id}: route outside diagram`);
        for (const heading of headings)
          if (crosses(a, b, heading, 2)) issues.push(`${edge.id}: crosses responsibility heading`);
        const length = Math.hypot(b.x - a.x, b.y - a.y);
        for (const node of nodes) {
          const shape = shapeFor(node);
          if (!shape) continue;
          const inverse = shape.getScreenCTM().inverse();
          for (let offset = 2; offset < length - 1; offset += 2) {
            const point = new DOMPoint(
              a.x + (b.x - a.x) * offset / length,
              a.y + (b.y - a.y) * offset / length,
            ).matrixTransform(inverse);
            if (shape.isPointInFill(point)) {
              issues.push(`${edge.id}: crosses node ${node.dataset.component}`);
              break;
            }
          }
        }
      }
    }
    for (let i = 0; i < labels.length; i++) {
      const label = labels[i], id = label.dataset.edgeLabel;
      const edge = model.edges.find((e) => e.id === id), box = rect(label);
      if (!edge || !label.textContent.trim())
        issues.push(`${id}: relationship caption is empty or unresolved`);
      if (box.left < bounds.left || box.right > bounds.right ||
          box.top < bounds.top || box.bottom > bounds.bottom)
        issues.push(`${id}: caption outside diagram`);
      for (const node of nodes)
        if (shapeOverlapsRect(shapeFor(node), box, 2))
          issues.push(`${id}: caption overlaps node ${node.dataset.component}`);
      for (const heading of headings)
        if (overlaps(box, heading, 2)) issues.push(`${id}: caption overlaps responsibility heading`);
      for (const other of labels.slice(i + 1))
        if (overlaps(box, rect(other), 2)) issues.push(`${id}: caption overlaps ${other.dataset.edgeLabel}`);
      for (const route of renderedPaths)
        for (let j = 1; j < route.points.length; j++)
          if (crosses(route.points[j - 1], route.points[j], box, 1))
            issues.push(`${id}: caption obscures route ${route.id}`);
    }
    for (const node of model.components) {
      const incoming = renderedPaths.filter((r) => model.edges.find((e) => e.id === r.id)?.to === node.id);
      for (let i = 0; i < incoming.length; i++)
        for (const other of incoming.slice(i + 1)) {
          const a = incoming[i].points.at(-1), b = other.points.at(-1);
          if (Math.hypot(a.x - b.x, a.y - b.y) < 5)
            issues.push(`${node.id}: incoming relationships share a port`);
        }
    }
    if (document.documentElement.scrollWidth > innerWidth + 1)
      issues.push('Horizontal page overflow');
    return {
      issues: [...new Set(issues)], nodeCount: nodes.length,
      edgeCount: paths.length, captionCount: labels.length,
    };
  });
};
