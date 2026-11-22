// Design Judge rendered alignment measurement for references/visual-standards.md#alignment.
//
//   window.__designJudge.measure()
//
// Containers are landmarks, toolbars and painted surfaces. Each ink item (text run, graphic,
// painted control) belongs to its nearest container. Lines are where most rows sit; one table or
// list casts one vote, and a box enclosing other ink (a card or list row) votes with its edge while
// its contents are checked. Offsets run from the inline start (leading lines) or inline end
// (trailing lines). Rows that disagree with no majority derive no line. A container with no edge line
// is `unmeasured`: its edges are not checked, not passed (a bar's centring still is).
// Text is measured by its line boxes and graphics by their element boxes, not glyph outlines.
// Shadow DOM and iframes are not traversed.
(() => {
  const PASS_PX = 1; // more than 1px off a line is a miss
  const CONTROL_PX = 56; // largest control or mark; taller painted elements are surfaces
  const LIST_ROW_SHARE = 0.6; // a control wider than this share of its container is a list row
  const SPACER_PX = 16; // a gap at least this wide pushes the last item to the end; a centred row has none
  const LANDMARKS = "aside, nav, footer, dialog, [popover], [role=dialog], [role=menu], [role=listbox], [role=navigation], [role=toolbar], [role=tabpanel]";
  const BARS = "header, footer, nav, [role=navigation], [role=toolbar], [role=menubar]"; // where centring applies
  const COLLECTIONS = "table, [role=table], [role=grid], ul, ol, [role=list], [role=listbox], [role=menu]";
  const FIELDS = "button, select, textarea, input:not([type=hidden])";
  const OPAQUE_FIELDS = "select, textarea, input, [role=combobox]"; // bordered by default; contents are not measured
  const NOT_BOXES = "[role=tab], [role=tablist], table, tbody, thead, tr, td, th";
  const ROWS = "li, [role=listitem], [role=option], [role=row]"; // wide painted rows are list rows at any height
  const CELLS = "td, th, [role=cell], [role=gridcell], [role=columnheader], [role=rowheader]";
  const GUIDES = [
    ["text", "start", "rgba(235,64,52,0.9)"], ["label", "start", "rgba(235,64,52,0.9)"],
    ["box", "start", "rgba(235,64,52,0.45)"], ["iconCentre", "start", "rgba(235,64,52,0.3)"],
    ["trailing", "end", "rgba(33,150,243,0.9)"], ["trailingCentre", "end", "rgba(255,179,0,0.8)"],
  ];
  const MISS_COLOUR = "rgba(214,0,170,0.95)";

  const toHalfPx = (n) => Math.round(n * 2) / 2;
  const css = (el) => getComputedStyle(el);
  const px = (el, property) => parseFloat(css(el).getPropertyValue(property)) || 0;
  const widthOf = (item) => item.right - item.left;

  // Alpha channel of a computed colour: rgb(), rgba(), and space-separated "… / a" forms.
  const alphaOf = (colour) => {
    if (!colour || colour === "transparent") return 0;
    const slash = colour.match(/\/\s*([\d.]+)(%?)\s*\)$/);
    if (slash) return parseFloat(slash[1]) / (slash[2] ? 100 : 1);
    const parts = colour.match(/^rgba?\(([^)]*)\)$/)?.[1].split(",");
    return parts && parts.length === 4 ? parseFloat(parts[3]) : 1;
  };
  const painted = (el) => {
    const s = css(el);
    if (alphaOf(s.backgroundColor) > 0 || (s.boxShadow && s.boxShadow !== "none")) return true;
    return ["top", "right", "bottom", "left"].every(
      (side) => px(el, `border-${side}-width`) > 0 && alphaOf(s.getPropertyValue(`border-${side}-color`)) > 0,
    );
  };
  const visible = (el) => {
    const s = css(el);
    return s.display !== "none" && s.visibility !== "hidden" && parseFloat(s.opacity) > 0;
  };
  // Visually hidden helpers (sr-only text, clipped to a pixel or less) carry no visible ink.
  // aria-hidden does not hide anything visually, so decorative icons are still measured.
  const visuallyHidden = (el) => {
    if (el.closest("[data-dj-overlay]")) return true;
    for (let node = el, depth = 0; node && depth < 4; node = node.parentElement, depth++) {
      const r = node.getBoundingClientRect();
      if ((r.width <= 1 || r.height <= 1) && css(node).display !== "contents") return true;
    }
    return false;
  };
  const ancestorsWithin = (el, container) => {
    const chain = [];
    for (let node = el.parentElement; node && node !== container; node = node.parentElement) chain.push(node);
    return chain;
  };
  const outermostWithin = (el, container, selector) =>
    [el, ...ancestorsWithin(el, container)].reverse().find((node) => node.matches(selector)) || null;
  const wideRow = (el) => el.matches(ROWS) && el.getBoundingClientRect().width > LIST_ROW_SHARE * (el.parentElement?.getBoundingClientRect().width || 0);
  const encloses = (outer, inner) => outer !== inner && inner.left >= outer.left - PASS_PX && inner.right <= outer.right + PASS_PX &&
    inner.top >= outer.top - PASS_PX && inner.bottom <= outer.bottom + PASS_PX;

  // An in-page header, footer or nav (a card footer, a breadcrumb) is part of the page.
  const isLandmark = (el) => (el.matches(LANDMARKS) || el.matches("header")) &&
    !(el.matches("header, footer, nav") && el.parentElement?.closest("main, article, section, [role=main]"));
  const findContainers = () => {
    const candidates = [...document.body.querySelectorAll("*")].filter((el) =>
      isLandmark(el) || (!el.matches(NOT_BOXES) && !wideRow(el) && el.getBoundingClientRect().height > CONTROL_PX && painted(el)));
    return candidates.filter((el) => {
      const r = el.getBoundingClientRect();
      return r.width > 120 && r.height > 24 && visible(el) && !visuallyHidden(el);
    });
  };

  // A control is a bordered field, or painted and control-sized (or a painted list row). Unpainted
  // buttons are not controls: their text and icons are the ink people see.
  const isControl = (el) => !el.matches(NOT_BOXES) &&
    (el.matches(OPAQUE_FIELDS) || (painted(el) && (el.getBoundingClientRect().height <= CONTROL_PX || wideRow(el))));

  const inkItem = (rect, kind, text, el) => ({
    kind, el, text: (text || "").trim().replace(/\s+/g, " ").slice(0, 24),
    top: rect.top, bottom: rect.bottom, left: rect.left, right: rect.right, mid: (rect.top + rect.bottom) / 2,
  });

  const collectInk = (containers) => {
    const owned = new Set(containers);
    const ink = new Map(containers.map((c) => [c, []]));
    const frameOf = new Map(containers.map((c) => [c, c.getBoundingClientRect()]));
    const recorded = new Set();
    const ownerOf = (el) => {
      for (let node = el; node; node = node.parentElement) if (owned.has(node)) return node;
      return null;
    };
    // Ink outside its container, clipped by a scrolling ancestor, or inside a sideways scroller
    // (positioned wherever it was scrolled) has no stable line.
    const measurable = (el, owner) => {
      const rect = el.getBoundingClientRect();
      if (!encloses(frameOf.get(owner), rect)) return false;
      for (let node = el; node && node !== owner.parentElement; node = node.parentElement) {
        const s = css(node);
        if (s.overflow !== "visible" && !encloses(node.getBoundingClientRect(), rect)) return false;
        if (/auto|scroll/.test(s.overflowX) && node.scrollWidth > node.clientWidth + 1) return false;
      }
      return true;
    };
    // The outermost control absorbs the ink inside it; a list row (wide, and not a button, a group of
    // buttons, a field or a field's wrapper such as a bordered search box) also keeps it.
    const add = (el, makeItem) => {
      const owner = ownerOf(el);
      if (!owner || !measurable(el, owner)) return;
      let control = null;
      for (let node = el; node && node !== owner; node = node.parentElement) if (isControl(node)) control = node;
      if (control && !recorded.has(control)) {
        recorded.add(control);
        const name = control.getAttribute("aria-label") || control.textContent || control.getAttribute("name") || control.tagName.toLowerCase();
        ink.get(owner).push(inkItem(control.getBoundingClientRect(), "box", `[${name.trim().slice(0, 20)}]`, control));
      }
      const fieldLike = control && (control.matches(OPAQUE_FIELDS) || control.querySelector(OPAQUE_FIELDS));
      const buttons = control && (control.matches("button, [role=button]") || [...control.children].every((c) => c.matches("button, [role=button], [role=tab]")));
      const listRow = control && !fieldLike && !buttons && control.getBoundingClientRect().width > frameOf.get(owner).width * LIST_ROW_SHARE;
      if (makeItem && (!control || listRow)) ink.get(owner).push(makeItem());
    };

    const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
    for (let node = walker.nextNode(); node; node = walker.nextNode()) {
      const parent = node.parentElement;
      if (!node.textContent.trim() || !parent || !visible(parent) || visuallyHidden(parent)) continue;
      const range = document.createRange();
      range.selectNodeContents(node);
      // Lines after a text node's first line are wrapped continuations: they neither vote nor are checked.
      [...range.getClientRects()].filter((r) => r.width > 1).forEach((rect, line) =>
        add(parent, () => ({ ...inkItem(rect, "text", node.textContent, parent), continues: line > 0 })));
    }
    const markSized = (r) => r.width > 1 && r.width <= CONTROL_PX && r.height <= CONTROL_PX;
    for (const el of document.body.querySelectorAll("svg, img, [role=img]")) {
      if (!visible(el) || visuallyHidden(el)) continue;
      const r = el.getBoundingClientRect();
      if (markSized(r)) add(el, () => inkItem(r, "graphic", `<${el.tagName.toLowerCase()}>`, el));
    }
    for (const el of document.body.querySelectorAll(FIELDS)) if (visible(el) && !visuallyHidden(el)) add(el, null);
    // Painted marks with no ink of their own, such as CSS avatars and status dots.
    for (const el of document.body.querySelectorAll("*")) {
      if (el.childElementCount || el.textContent.trim() || !visible(el) || visuallyHidden(el)) continue;
      const r = el.getBoundingClientRect();
      if (markSized(r) && Math.min(r.width, r.height) >= 4 && painted(el)) add(el, null);
    }
    return ink;
  };

  // Text joins a row only beside text it overlaps vertically, so stacked lines stay separate.
  // A box enclosing other ink (a card or list row) joins the row of its first content without
  // stretching it.
  const overlaps = (a, b) => Math.min(a.bottom, b.bottom) > Math.max(a.top, b.top);
  const groupRows = (items) => {
    const rows = [];
    for (const item of items.filter((i) => !i.wraps).sort((a, b) => a.mid - b.mid)) {
      const fits = (row) => item.mid >= row.top && item.mid <= row.bottom &&
        (item.kind !== "text" || row.items.every((o) => o.kind !== "text" || overlaps(o, item)));
      let row = rows.find(fits);
      if (!row) rows.push((row = { top: item.top, bottom: item.bottom, items: [] }));
      row.items.push(item);
      row.top = Math.min(row.top, item.top);
      row.bottom = Math.max(row.bottom, item.bottom);
    }
    for (const box of items.filter((i) => i.wraps)) {
      const home = rows.filter((r) => r.items.some((i) => box.covers(i))).sort((a, b) => a.top - b.top)[0];
      if (home) home.items.push(box);
      else rows.push({ top: box.top, bottom: box.bottom, items: [box] });
    }
    return rows;
  };

  // The position most rows share, clustered within PASS_PX. Entries carry a vote key: one table or
  // list is one vote. Ties go to the line page-level rows sit on, then to the larger cluster, then to
  // ink over card edges, then to the container's padding edge. Clusters still tied leave no line:
  // with no majority, neither side is the outlier.
  // A line needs `minEntries` in the container and `minMembers` on it. Text and trailing lines accept
  // a single page row (a title) as the line; centre and label lines need two rows, so no row passes itself.
  const outranks = (a, b) => {
    const i = a.findIndex((value, index) => value !== b[index]);
    return i >= 0 && a[i] > b[i];
  };
  const sharedLine = (entries, { minEntries = 2, minMembers = 2, padding } = {}) => {
    const valid = entries.filter((e) => Number.isFinite(e.v));
    if (valid.length < minEntries) return undefined;
    let best = null;
    for (const { v: start } of valid) {
      const members = valid.filter((e) => e.v >= start && e.v - start <= PASS_PX);
      if (members.length < minMembers) continue;
      const score = [new Set(members.map((e) => e.key)).size, members.some((e) => !e.collection) ? 1 : 0, members.length,
        members.some((e) => !e.edge) ? 1 : 0, Math.abs(start - padding) <= PASS_PX ? 1 : 0];
      if (!best || outranks(score, best.score)) best = { score, members, tied: false };
      else if (!outranks(best.score, score) && !members.some((e) => best.members.includes(e))) best.tied = true;
    }
    if (!best || best.tied) return undefined;
    const sorted = best.members.map((e) => e.v).sort((a, b) => a - b);
    return sorted[Math.floor(sorted.length / 2)];
  };

  const analyse = (container, items) => {
    const frame = container.getBoundingClientRect();
    const rtl = css(container).direction === "rtl";
    const fromStart = (it) => toHalfPx(rtl ? frame.right - it.right : it.left - frame.left);
    const fromEnd = (it) => toHalfPx(rtl ? it.left - frame.left : frame.right - it.right);
    const inset = (side) => px(container, `border-${side}-width`) + px(container, `padding-${side}`);
    const padStart = inset(rtl ? "right" : "left");
    const padEnd = inset(rtl ? "left" : "right");
    // Icons drawn over a field (a search glyph in an input) are part of that field.
    const fields = items.filter((i) => i.kind === "box" && i.el.matches(OPAQUE_FIELDS));
    items = items.filter((i) => i.kind === "box" || !fields.some((f) => encloses(f, i)));
    for (const box of items.filter((i) => i.kind === "box")) {
      box.covers = (o) => o !== box && encloses(box, o) && !(o.kind === "box" && encloses(o, box)); // identical boxes do not wrap each other
      box.wraps = items.some(box.covers);
    }
    const insideWrapper = (item) => items.some((b) => b.wraps && b.covers(item));

    const rows = groupRows(items).map((group) => {
      const ordered = [...group.items].sort((a, b) => fromStart(a) - fromStart(b));
      const content = ordered.filter((i) => !i.wraps);
      const box = ordered[0].kind === "box" ? ordered[0] : undefined;
      const first = ordered.find((i) => i.kind !== "box");
      const firstLeads = first && !first.continues && (ordered[0] === first || box?.wraps);
      const last = content[content.length - 1] || ordered[0];
      // A marker (graphic, or a box no wider than a control, such as an avatar) followed by text sets the label line.
      const candidate = box?.wraps ? first : ordered[0];
      const marker = candidate && (candidate.kind === "graphic" || (candidate.kind === "box" && widthOf(candidate) <= CONTROL_PX)) ? candidate : undefined;
      const label = marker && ordered.find((i) => i.kind === "text");
      // The last item trails when it ends in the last quarter of a row split by a spacer gap (a packed
      // action group after a title trails as one); text trails only when its element shrink-wraps it, so a
      // stretched value column does not. A row starting in the right
      // half, or a table cell, trails only when its last item is end-aligned: ragged text does not trail.
      const gaps = content.slice(1).map((it, i) => fromStart(it) - (fromStart(content[i]) + widthOf(content[i])));
      // A row starting in the right half, or inside a group pushed to the end (a wrapped pagination), starts late.
      const start = content[0] || ordered[0];
      const startsLate = fromStart(start) > frame.width / 2 ||
        ancestorsWithin(start.el, container).some((a) => /flex|grid/.test(css(a).display) && !/column/.test(css(a).flexDirection) && /end|right/.test(css(a).justifyContent));
      const endAligned = last.kind !== "text" || /right|end/.test(css(last.el).textAlign);
      const shrinkWrapped = last.kind !== "text" || Math.abs(fromEnd(last.el.getBoundingClientRect()) - fromEnd(last)) <= PASS_PX;
      const trails = fromEnd(last) < frame.width / 4 && (startsLate || last.el.closest?.(CELLS) ? endAligned : shrinkWrapped && gaps.some((g) => g >= SPACER_PX));
      const span = content.length ? (Math.min(...content.map((i) => i.left)) + Math.max(...content.map((i) => i.right))) / 2 : NaN;
      return {
        y: toHalfPx(group.top - frame.top), top: group.top, bottom: group.bottom, ordered, content, box, first, last, marker, label, trails, startsLate,
        // Only lists with visible markers indent their text; unmarked UI lists sit on the text line.
        depth: first ? ancestorsWithin(first.el, container).filter((a) => a.matches("ul, ol") && css(a).listStyleType !== "none").length : 0,
        collection: outermostWithin((first || box).el, container, COLLECTIONS),
        lead: firstLeads ? fromStart(first) : undefined,
        boxLead: box ? fromStart(box) : undefined,
        boxPadding: box ? px(box.el, rtl ? "padding-right" : "padding-left") : 0,
        labelAt: label ? fromStart(label) : undefined,
        iconCentre: label ? toHalfPx(fromStart(marker) + widthOf(marker) / 2) : undefined,
        end: trails ? fromEnd(last) : undefined,
        endCentre: trails ? toHalfPx(fromEnd(last) + widthOf(last) / 2) : undefined,
        // A centred row is one group, clear of the padding edge, centred in the container.
        centred: !trails && !gaps.some((g) => g >= SPACER_PX) && fromStart(content[0] || ordered[0]) > padStart + PASS_PX &&
          Math.abs(span - (frame.left + frame.right) / 2) <= PASS_PX,
      };
    });
    // Text stacked beside a marker row (an email under a name beside an avatar) belongs to its label line.
    for (const row of rows) {
      row.stackedIn = rows.find((o) => o !== row && overlaps(o, row) && o.labelAt !== undefined && row.lead !== undefined && row.lead >= o.labelAt - PASS_PX);
    }

    const lines = deriveLines(rows, { frame, fromEnd, insideWrapper, padStart, padEnd });
    const misses = checkRows(container, rows, lines, fromStart);
    return { container, frame, rtl, lines, misses: mergeMisses(misses) };
  };

  const vote = (row, v, edge = false) => ({ v, key: row.collection || row, collection: row.collection, edge });

  const deriveLines = (rows, { frame, fromEnd, insideWrapper, padStart, padEnd }) => {
    const voters = rows.filter((r) => r.depth === 0 && !r.startsLate && !r.stackedIn && !r.centred);
    // Text inside a card or list row is checked against the line; the card's edge votes instead.
    const textFromRows = sharedLine([
      ...voters.filter((r) => r.lead !== undefined && !insideWrapper(r.first)).map((r) => vote(r, r.lead)),
      ...voters.filter((r) => r.box?.wraps).map((r) => vote(r, r.boxLead, true)),
    ], { minMembers: 1, padding: padStart });
    const trailingRows = rows.filter((r) => r.trails && !insideWrapper(r.last));
    const trailingFromRows = sharedLine([
      ...trailingRows.map((r) => vote(r, r.end)),
      ...rows.filter((r) => r.box?.wraps && fromEnd(r.box) < frame.width / 4).map((r) => vote(r, fromEnd(r.box), true)),
    ], { minMembers: 1, padding: padEnd });
    const lines = {
      text: textFromRows,
      label: sharedLine(rows.map((r) => vote(r, r.labelAt))),
      iconCentre: sharedLine(rows.map((r) => vote(r, r.iconCentre))),
      trailing: trailingFromRows,
      // Trailing controls and icons of different widths may centre on one line; text may not.
      trailingCentre: sharedLine(trailingRows.filter((r) => r.last.kind !== "text").map((r) => vote(r, r.endCentre))),
    };
    // The box line is the text line minus a control's padding, so its label continues the text line.
    // Without a text line (a stack of controls), it is where most controls start.
    const boxLine = (r) => toHalfPx(lines.text - r.boxPadding);
    lines.box = lines.text === undefined
      ? sharedLine(rows.filter((r) => r.box && !r.startsLate).map((r) => vote(r, r.boxLead)))
      : sharedLine(rows.filter((r) => r.box && Math.abs(r.boxLead - boxLine(r)) <= PASS_PX).map((r) => vote(r, boxLine(r))), { minEntries: 1, minMembers: 1 });
    const nested = {};
    for (const depth of new Set(rows.map((r) => r.depth).filter((d) => d > 0))) {
      nested[depth] = sharedLine(rows.filter((r) => r.depth === depth).map((r) => vote(r, r.lead)));
    }
    return { ...lines, nested };
  };

  const checkRows = (container, rows, lines, fromStart) => {
    const misses = [];
    const near = (value, line) => line !== undefined && Math.abs(value - line) <= PASS_PX;
    const nearest = (value, candidates) => candidates.filter((l) => l !== undefined).sort((a, b) => Math.abs(value - a) - Math.abs(value - b))[0];
    const report = (row, edge, item, value, expected) => misses.push({ row, edge, item, px: value, expected, delta: toHalfPx(value - expected) });
    const byTop = [...rows].sort((a, b) => a.top - b.top);
    // Text starting under a later item of the row just above (helper text under a field) follows that column.
    const underColumn = (row) => {
      const above = byTop[byTop.indexOf(row) - 1];
      return above?.content.some((i) => i !== above.content[0] && i.kind !== "box" && Math.abs(fromStart(i) - row.lead) <= PASS_PX);
    };
    const inBar = container.matches(BARS);
    for (const row of rows) {
      const leading = !row.startsLate && !row.centred;
      if (leading && row.box && (lines.text ?? lines.box) !== undefined) {
        const permitted = [lines.text, lines.label, lines.box];
        if (!permitted.some((l) => near(row.boxLead, l))) report(row, "box", row.box, row.boxLead, nearest(row.boxLead, permitted));
      }
      // A row may start on the text or label line; an icon centred on the icon column passes whatever its width.
      const onIconColumn = row.marker === row.first && near(row.iconCentre, lines.iconCentre);
      if (leading && row.lead !== undefined && !onIconColumn) {
        const expected = row.stackedIn ? row.stackedIn.labelAt : row.depth === 0 ? (lines.text === undefined ? undefined : nearest(row.lead, [lines.text, lines.label])) : lines.nested[row.depth];
        if (expected !== undefined && !near(row.lead, expected) && !underColumn(row)) report(row, "leading", row.first, row.lead, expected);
      }
      if (row.labelAt !== undefined && lines.label !== undefined && !near(row.labelAt, lines.label))
        report(row, "label", row.label, row.labelAt, lines.label);
      if (row.iconCentre !== undefined && lines.iconCentre !== undefined && !near(row.iconCentre, lines.iconCentre))
        report(row, "icon-column", row.marker, row.iconCentre, lines.iconCentre);
      if (row.trails && lines.trailing !== undefined && !near(row.end, lines.trailing) && !near(row.endCentre, lines.trailingCentre))
        report(row, "trailing", row.last, row.end, lines.trailing);
      // Centring is a bar and toolbar rule.
      if (inBar && row.content.length > 1 && !rows.some((o) => o !== row && overlaps(o, row))) {
        const mids = row.content.map((i) => i.mid).sort((a, b) => a - b);
        const median = mids[Math.floor(mids.length / 2)];
        const worst = row.content.reduce((a, b) => (Math.abs(b.mid - median) > Math.abs(a.mid - median) ? b : a));
        if (Math.abs(worst.mid - median) > PASS_PX) report(row, "vertical-centre", worst, toHalfPx(worst.mid - median), 0);
      }
    }
    return misses;
  };

  // One finding per cause: misses with the same offset in one row, table or list merge, counting rows.
  const mergeMisses = (misses) => {
    const findings = [];
    for (const m of misses) {
      const owner = m.row.collection || m.row;
      const same = findings.find((f) => f.owner === owner && f.delta === m.delta);
      if (same) {
        same.rows.add(m.row);
        if (!same.edges.includes(m.edge)) same.edges.push(m.edge);
      } else findings.push({ ...m, owner, rows: new Set([m.row]), edges: [m.edge] });
    }
    return findings.map((f) => ({ ...f, edges: f.edges.sort(), count: f.rows.size }));
  };

  const describe = (el) =>
    el.getAttribute("aria-label") || el.querySelector("h1, h2, h3, h4, [role=heading]")?.textContent.trim().slice(0, 40) ||
    el.id || el.innerText?.trim().replace(/\s+/g, " ").slice(0, 30) || el.tagName.toLowerCase();

  const drawOverlay = (results) => {
    document.querySelectorAll("[data-dj-overlay]").forEach((n) => n.remove());
    const docWidth = document.documentElement.scrollWidth, docHeight = document.documentElement.scrollHeight;
    const layer = document.createElement("div");
    layer.dataset.djOverlay = "";
    // The layer never widens the page it measures.
    Object.assign(layer.style, { position: "absolute", left: "0", top: "0", width: `${docWidth}px`, height: `${docHeight}px`, overflow: "hidden", pointerEvents: "none", zIndex: 2147483647 });
    document.body.appendChild(layer); // attached first, so label widths can be measured
    const sx = window.scrollX, sy = window.scrollY;
    const shape = (style) => {
      const d = document.createElement("div");
      Object.assign(d.style, { position: "absolute" }, style);
      return layer.appendChild(d);
    };
    for (const { frame, lines, rtl, misses } of results) {
      for (const [key, side, colour] of GUIDES) {
        if (lines[key] === undefined) continue;
        const x = (side === "start") !== rtl ? frame.left + lines[key] : frame.right - lines[key];
        shape({ left: `${x + sx}px`, top: `${frame.top + sy}px`, height: `${frame.height}px`, borderLeft: `1px dashed ${colour}` });
      }
      for (const m of misses) {
        const it = m.item;
        shape({ left: `${it.left + sx - 2}px`, top: `${it.top + sy - 2}px`, width: `${widthOf(it) + 4}px`, height: `${it.bottom - it.top + 4}px`, outline: `1px solid ${MISS_COLOUR}` });
        const tag = shape({ top: `${it.mid + sy - 7}px`, font: "10px/14px ui-monospace, monospace", color: "#fff", background: MISS_COLOUR, padding: "0 4px", whiteSpace: "nowrap" });
        tag.textContent = `${m.edges.join("+")} ${m.delta > 0 ? "+" : ""}${m.delta}px${m.count > 1 ? ` x${m.count}` : ""}`;
        const fitsRight = it.right + sx + 6 + tag.offsetWidth <= docWidth;
        tag.style.left = `${fitsRight ? it.right + sx + 6 : Math.max(0, it.left + sx - 6 - tag.offsetWidth)}px`;
      }
    }
  };

  window.__designJudge = {
    measure() {
      const containers = findContainers();
      const ink = collectInk(containers);
      const results = containers.map((c) => analyse(c, ink.get(c)));
      drawOverlay(results);
      return results.map(({ container, frame, rtl, lines, misses }) => {
        const { nested, ...main } = lines;
        return {
          container: describe(container),
          direction: rtl ? "rtl" : "ltr",
          frame: { x: toHalfPx(frame.left + window.scrollX), y: toHalfPx(frame.top + window.scrollY), width: toHalfPx(frame.width), height: toHalfPx(frame.height) },
          unmeasured: [...Object.values(main), ...Object.values(nested)].every((line) => line === undefined),
          lines: main,
          misses: misses.map((m) => ({ edges: m.edges, item: m.item.text, y: m.row.y, px: m.px, expected: m.expected, delta: m.delta, count: m.count })),
        };
      });
    },
  };
})();
