const TYPE_LABELS = {
  work: "Entry skill",
  skill: "Skill",
  playbook: "aapilot playbook",
  principle: "Approved principle",
  foundation: "Shared foundation",
  artifact: "Project-owned records",
  role: "Agent role",
};

const nodes = [
  {
    id: "work",
    title: "aapilot",
    type: "work",
    subtitle: "Fundamental entry point",
    purpose: "Selects the path, keeps one owner, coordinates supporting skills, and remains accountable through verification and delivery.",
    owns: "Task framing, routing, integration, final proof, and completion.",
    source: "../../skills/aapilot/SKILL.md",
    x: -310,
    y: 530,
    w: 240,
    h: 122,
  },
  {
    id: "product",
    title: "Product",
    type: "skill",
    subtitle: "Meaning & behavior",
    purpose: "Discovers journeys and defines intended behavior, business rules, invariants, and acceptance scenarios.",
    owns: "Business meaning and the scoped product behavior contract.",
    source: "../../skills/product/SKILL.md",
    x: 430,
    y: 55,
  },
  {
    id: "solution",
    title: "Solution",
    type: "skill",
    subtitle: "Overall direction",
    purpose: "Researches and compares overall approaches while the problem, ownership, trust model, or direction remains open.",
    owns: "The solution decision, its rationale, and conditions for reconsideration.",
    source: "../../skills/solution/SKILL.md",
    x: 879,
    y: 55,
  },
  {
    id: "interaction-design",
    title: "Interaction design",
    type: "skill",
    subtitle: "Experience structure",
    purpose: "Turns product outcomes into navigation, interaction, and information-visibility decisions.",
    owns: "The interaction model and presentation rationale for its assigned scope.",
    source: "../../skills/interaction-design/SKILL.md",
    x: 1327,
    y: 55,
  },
  {
    id: "ui-refinement",
    title: "UI refinement",
    type: "skill",
    subtitle: "Human review loop",
    purpose: "Coordinates a bounded UI/UX refinement cycle and returns an identifiable reviewed visual reference.",
    owns: "The refinement checkpoint and reviewed-reference handoff; the caller retains production delivery.",
    source: "../../skills/ui-refinement/SKILL.md",
    x: 1776,
    y: 55,
  },
  {
    id: "architect",
    title: "Architect",
    type: "skill",
    subtitle: "Implementation shape",
    purpose: "Designs caller usage, data shapes, signatures, ownership, and module boundaries; plans proof and revises the design when the caller returns contradictory evidence.",
    owns: "The design trigger, implementation design, rationale, and proof plan; returns a design package to the caller.",
    source: "../../skills/architect/SKILL.md",
    x: 2224,
    y: 55,
  },
  {
    id: "grill-me",
    title: "Grill me",
    type: "skill",
    subtitle: "Dependent user choices",
    purpose: "Interviews the user one question at a time when several consequential choices depend on their judgment.",
    owns: "Interview conduct and attributable evidence; its caller owns synthesis.",
    source: "../../skills/grill-me/SKILL.md",
    x: 430,
    y: 165,
  },
  {
    id: "domain-modeling",
    title: "Domain modeling",
    type: "skill",
    subtitle: "Terms & decisions",
    purpose: "Clarifies project concepts and preserves established terminology or qualifying decisions with their standing and authority.",
    owns: "Glossary meaning and scoped product, design, or software decision records.",
    source: "../../skills/domain-modeling/SKILL.md",
    x: 879,
    y: 165,
  },
  {
    id: "investigation",
    title: "Investigation",
    type: "playbook",
    subtitle: "Explain without changing",
    purpose: "Produces a cited explanation or recommendation while preserving a read-only boundary.",
    owns: "The investigation question, evidence reconciliation, and bounded conclusion.",
    source: "../../skills/aapilot/playbooks/investigation.md",
    x: 430,
    y: 345,
  },
  {
    id: "how",
    title: "How",
    type: "skill",
    subtitle: "Current mechanics",
    purpose: "Traces an existing subsystem from entry point through calls, state changes, boundaries, and visible effects.",
    owns: "The evidence-backed explanation of current behavior.",
    source: "../../skills/how/SKILL.md",
    x: 879,
    y: 345,
  },
  {
    id: "why",
    title: "Why",
    type: "skill",
    subtitle: "Historical rationale",
    purpose: "Reconstructs why an existing design took its shape and calibrates claims to the available historical evidence.",
    owns: "The rationale chronology, evidence confidence, and surviving constraints.",
    source: "../../skills/why/SKILL.md",
    x: 1327,
    y: 345,
  },
  {
    id: "probe",
    title: "Probe",
    type: "skill",
    subtitle: "Empirical unknown",
    purpose: "Runs the smallest credible observation or experiment that could change a consequential decision.",
    owns: "The empirical method, observed result, confidence, and limits.",
    source: "../../skills/probe/SKILL.md",
    x: 1776,
    y: 345,
  },
  {
    id: "prototype-playbook",
    title: "Prototype",
    type: "playbook",
    subtitle: "Decision experiment",
    purpose: "Coordinates a bounded experiment whose output is evidence and a recommendation, not production implementation.",
    owns: "The decision the experiment resolves and the handoff of its evidence.",
    source: "../../skills/aapilot/playbooks/prototype.md",
    x: 430,
    y: 455,
  },
  {
    id: "prototype",
    title: "Prototype artifact",
    type: "skill",
    subtitle: "Inspectable model",
    purpose: "Builds and exercises a throwaway business-state walkthrough, rendered candidate, or contextual UI comparison.",
    owns: "The inspectable artifact and its observations; the caller owns the larger decision.",
    source: "../../skills/prototype/SKILL.md",
    x: 879,
    y: 455,
  },
  {
    id: "arena",
    title: "Arena",
    type: "skill",
    subtitle: "Competing alternatives",
    purpose: "Generates genuinely different candidates, judges them, selects a base, and synthesizes compatible strengths.",
    owns: "Candidate comparison and one coherent synthesized result.",
    source: "../../skills/arena/SKILL.md",
    x: 1327,
    y: 455,
  },
  {
    id: "interrogate",
    title: "Interrogate",
    type: "skill",
    subtitle: "Adversarial review",
    purpose: "Reviews consequential work from several lenses, checks claims, and returns deduplicated weaknesses and risks.",
    owns: "The assessment; the requesting owner decides and performs fixes.",
    source: "../../skills/interrogate/SKILL.md",
    x: 1776,
    y: 455,
  },
  {
    id: "maintainability",
    title: "Maintainability",
    type: "skill",
    subtitle: "Reader & change burden",
    purpose: "Assesses whether supplied code or a design is easy to understand, change, and verify, then returns concrete findings to its caller.",
    owns: "The bounded assessment and its evidence-backed findings; the caller decides on design, edits, and records.",
    source: "../../skills/maintainability/SKILL.md",
    x: 2224,
    y: 455,
  },
  {
    id: "feature",
    title: "Feature",
    type: "playbook",
    subtitle: "Change behavior",
    purpose: "Grounds, designs, implements, verifies, and delivers an intentional behavior change.",
    owns: "Feature execution, acceptance criteria, integration, and final behavioral proof.",
    source: "../../skills/aapilot/playbooks/feature.md",
    x: 430,
    y: 635,
  },
  {
    id: "bug-fix",
    title: "Bug fix",
    type: "playbook",
    subtitle: "Correct a mechanism",
    purpose: "Reproduces a failure, confirms its cause, implements a bounded correction, and replays the original surface.",
    owns: "Reproduction, causal diagnosis, correction, and failing-before/passing-after proof.",
    source: "../../skills/aapilot/playbooks/bug-fix.md",
    x: 430,
    y: 745,
  },
  {
    id: "refactoring",
    title: "Refactoring",
    type: "playbook",
    subtitle: "Preserve behavior",
    purpose: "Changes structure in verifiable increments while holding the observed behavior contract constant.",
    owns: "The structural improvement and equivalence proof.",
    source: "../../skills/aapilot/playbooks/refactoring.md",
    x: 1776,
    y: 745,
  },
  {
    id: "figure-it-out",
    title: "Figure it out",
    type: "skill",
    subtitle: "No playbook fits",
    purpose: "Constructs a bounded, evidence-gated procedure when no bundled playbook fits or several phases are tightly coupled.",
    owns: "The custom procedure, phase gates, and checkable completion predicate.",
    source: "../../skills/figure-it-out/SKILL.md",
    x: 879,
    y: 635,
  },
  {
    id: "swarm",
    title: "Swarm",
    type: "skill",
    subtitle: "Slices & races",
    purpose: "Partitions independent work or runs declared races, accounts for every result, and returns one integrated report.",
    owns: "Coverage, worker boundaries, pre-result race criteria, aggregation, and combined verification.",
    source: "../../skills/swarm/SKILL.md",
    x: 1327,
    y: 635,
  },
  {
    id: "tdd",
    title: "TDD",
    type: "skill",
    subtitle: "Regression first",
    purpose: "Establishes a focused failing-before check and verifies it after a correction.",
    owns: "The regression check and its ordered failing/passing evidence.",
    source: "../../skills/tdd/SKILL.md",
    x: 879,
    y: 745,
  },
  {
    id: "show-work",
    title: "Show me your work",
    type: "skill",
    subtitle: "Decision trail",
    purpose: "Maintains an evidence-linked decision log for substantial, multi-phase, or unattended work.",
    owns: "The local audit trail and its retention boundary.",
    source: "../../skills/show-me-your-work/SKILL.md",
    x: 1327,
    y: 745,
  },
  {
    id: "opening-pr",
    title: "Opening a PR",
    type: "playbook",
    subtitle: "Authorized delivery",
    purpose: "Reviews the complete change, prepares its history and reviewer brief, publishes, and verifies the PR state.",
    owns: "PR preparation and publication—not monitoring, merging, or deployment.",
    source: "../../skills/aapilot/playbooks/opening-a-pr.md",
    x: 1776,
    y: 635,
  },
  {
    id: "skill-authoring",
    title: "Skill authoring",
    type: "playbook",
    subtitle: "Change instructions",
    purpose: "Traces behavior from entry point, edits the owning instructions, validates the package, and exercises consequential changes.",
    owns: "The intended instruction behavior and its validation boundary.",
    source: "../../skills/aapilot/playbooks/authoring-a-skill.md",
    x: 2224,
    y: 745,
  },
  {
    id: "evaluation",
    title: "Evaluation",
    type: "playbook",
    subtitle: "Behavioral evidence",
    purpose: "Runs temporary instruction experiments in isolated contexts with blinded judging and evidence checked against predefined criteria.",
    owns: "Experiment design, evidence reconciliation, and the adoption recommendation.",
    source: "../../skills/aapilot/playbooks/eval.md",
    x: 2224,
    y: 635,
  },
  {
    id: "implement",
    title: "Implement",
    type: "skill",
    subtitle: "Bounded edits & checks",
    purpose: "Executes a supplied design or contract within assigned file ownership, runs development checks, and returns edits, evidence, and design concerns.",
    owns: "Bounded implementation and development evidence; the caller retains integration and final acceptance.",
    source: "../../skills/implement/SKILL.md",
    x: 1327,
    y: 855,
  },
  {
    id: "independent-verification",
    title: "Independent verification",
    type: "role",
    subtitle: "Separate verification worker",
    purpose: "Derives expectations from the authoritative contract and exercises the identified changed artifact using the project verifier procedure.",
    owns: "Observed verification results, failures, and gaps; returns evidence to the caller for acceptance and correction assignments.",
    source: "../../skills/aapilot/references/execution.md#independent-implementation-verification",
    x: 879,
    y: 1145,
    w: 270,
  },
  {
    id: "bootstrap-verification",
    title: "Bootstrap verification",
    type: "skill",
    subtitle: "Establish proof paths",
    purpose: "Creates or adopts a project-local verifier, feature map, operating procedure, and demonstrated readiness evidence.",
    owns: "Verification setup and declared coverage gaps.",
    source: "../../skills/bootstrap-verification/SKILL.md",
    x: 430,
    y: 1035,
  },
  {
    id: "maintain-verification",
    title: "Maintain verification",
    type: "skill",
    subtitle: "Keep proof usable",
    purpose: "Audits and repairs the project's feature map and verification procedures without redefining intended behavior.",
    owns: "Verifier/map drift, scoped repairs, and coverage reporting.",
    source: "../../skills/maintain-verification/SKILL.md",
    x: 879,
    y: 1035,
  },
  {
    id: "reflect",
    title: "Reflect",
    type: "skill",
    subtitle: "Turn learning into change",
    purpose: "Reviews session evidence, synthesizes findings, and routes accepted learning into skill edits or structural follow-ups.",
    owns: "Reflection synthesis and approved personal-principle changes.",
    source: "../../skills/reflect/SKILL.md",
    x: 1327,
    y: 1035,
  },
  {
    id: "project-records",
    title: "Project evidence",
    type: "artifact",
    subtitle: "Canonical records",
    purpose: "Represents project-owned requirements, decisions, design records, feature maps, verifier recipes, and retained proof.",
    owns: "Durable project context; individual skills own only their scoped contribution and handoff.",
    source: "../../SKILL_SYSTEM.md",
    x: 1776,
    y: 1035,
  },
  {
    id: "execution-contract",
    title: "Execution contract",
    type: "foundation",
    subtitle: "Applies to all procedures",
    purpose: "Defines ownership, handoffs, delegation decisions, result acceptance, completion, review context, verification through the project, evidence, and delivery.",
    owns: "The shared operating rules read by every procedural skill and worker.",
    source: "../../skills/aapilot/references/execution.md",
    x: 2224,
    y: 1035,
  },
  {
    id: "principles-index",
    title: "Principle index",
    type: "foundation",
    subtitle: "Judgment routing",
    purpose: "Matches situations to approved personal judgments and carries their scope and exceptions through handoffs.",
    owns: "The discovery and application rules for approved principle leaves.",
    source: "../../skills/principles/INDEX.md",
    x: 1327,
    y: 1145,
  },
  {
    id: "preserve-context",
    title: "Preserve decision context",
    type: "principle",
    subtitle: "Handoff integrity",
    purpose: "Keeps constraints, evidence limits, and acceptance criteria available when workflows or handoffs are simplified.",
    owns: "The judgment that local brevity must not break downstream decisions.",
    source: "../../skills/principle-preserve-decision-context/SKILL.md",
    x: 1776,
    y: 1145,
    w: 270,
  },
  {
    id: "ui-meaning",
    title: "UI meaning through structure",
    type: "principle",
    subtitle: "Structural clarity",
    purpose: "Prefers layout, grouping, and labelled controls over prose that merely repeats what an interface already conveys.",
    owns: "The judgment about structural UI meaning and its safety exceptions.",
    source: "../../skills/principle-ui-meaning-through-structure/SKILL.md",
    x: 2224,
    y: 1145,
    w: 270,
  },
].map((node) => ({ w: 230, h: 104, ...node }));

const edges = [];

function connect(from, to, type, label) {
  edges.push({ id: `${from}--${to}--${type}`, from, to, type, label });
}

// aapilot's explicit task router.
[
  ["product", "define product behavior"],
  ["interaction-design", "design interactions"],
  ["grill-me", "interview for choices"],
  ["domain-modeling", "clarify meaning"],
  ["investigation", "explain or research"],
  ["solution", "choose direction"],
  ["bug-fix", "correct a defect"],
  ["feature", "change behavior"],
  ["refactoring", "change structure"],
  ["ui-refinement", "refine with feedback"],
  ["prototype-playbook", "resolve by experiment"],
  ["skill-authoring", "change a skill"],
  ["evaluation", "evaluate instructions"],
  ["opening-pr", "publish a PR"],
  ["bootstrap-verification", "establish verification"],
  ["maintain-verification", "audit verification"],
  ["reflect", "capture learning"],
  ["figure-it-out", "construct a procedure"],
].forEach(([to, label]) => connect("work", to, "route", label));

// Product, solution, and interaction ownership.
connect("product", "how", "support", "grounds existing behavior");
connect("product", "why", "support", "checks consequential rationale");
connect("product", "domain-modeling", "support", "clarifies ambiguous terms");
connect("product", "probe", "support", "settles testable assumptions");
connect("product", "interrogate", "support", "challenges the contract");
connect("product", "grill-me", "support", "collects dependent choices");
connect("product", "interaction-design", "handoff", "returns behavior contract");

connect("solution", "product", "support", "fills behavior gaps");
connect("solution", "grill-me", "support", "resolves value judgments");
connect("solution", "domain-modeling", "support", "records decisions");
connect("solution", "how", "support", "maps current system");
connect("solution", "why", "support", "preserves rationale");
connect("solution", "probe", "support", "tests decisive claims");
connect("solution", "interaction-design", "support", "compares workflow implications");
connect("solution", "arena", "support", "compares approaches");
connect("solution", "interrogate", "support", "challenges direction");
connect("solution", "architect", "handoff", "passes chosen direction");

connect("interaction-design", "arena", "support", "compares interaction models");
connect("interaction-design", "prototype", "support", "renders inspectable options");
connect("interaction-design", "ui-refinement", "handoff", "returns review need via caller");
connect("interaction-design", "product", "handoff", "returns meaning changes via caller");
connect("interaction-design", "architect", "handoff", "returns feasibility via caller");
connect("interaction-design", "solution", "handoff", "reopens overall direction");

connect("ui-refinement", "how", "support", "checks current mechanics");
connect("ui-refinement", "why", "support", "checks consequential rationale");
connect("ui-refinement", "product", "support", "resolves business rules");
connect("ui-refinement", "interaction-design", "support", "owns interaction choices");
connect("ui-refinement", "prototype", "support", "builds rendered candidate");

connect("architect", "product", "handoff", "returns product-rule gaps");
connect("architect", "domain-modeling", "support", "clarifies concepts / ADRs");
connect("architect", "how", "support", "traces affected behavior");
connect("architect", "why", "support", "checks ownership history");
connect("architect", "interaction-design", "handoff", "returns unsettled interactions");
connect("architect", "arena", "support", "compares implementation shapes");
connect("architect", "interrogate", "support", "reviews contested design");
connect("architect", "maintainability", "support", "assesses candidate burden");

// Investigation and experiment mechanics.
connect("investigation", "how", "support", "grounds current behavior");
connect("investigation", "why", "support", "reconstructs rationale");
connect("investigation", "solution", "handoff", "opens a solution decision");
connect("investigation", "probe", "support", "tests an observable unknown");
connect("how", "probe", "support", "checks unresolved runtime claim");
connect("how", "why", "handoff", "separates mechanics from motive");
connect("why", "how", "support", "anchors current mechanics");
connect("why", "solution", "handoff", "supplies historical constraints");
connect("why", "architect", "handoff", "supplies layering constraints");
connect("arena", "probe", "support", "reconciles disputed evidence");
connect("interrogate", "probe", "support", "checks material claims");
connect("interrogate", "maintainability", "support", "checks maintainability claims");
connect("prototype-playbook", "probe", "support", "defines empirical method");
connect("prototype-playbook", "prototype", "support", "delegates inspectable artifact");
connect("prototype-playbook", "feature", "handoff", "passes selected direction");
connect("prototype-playbook", "architect", "handoff", "passes design evidence");
connect("prototype", "probe", "support", "uses empirical method");
connect("prototype", "interaction-design", "handoff", "returns interaction evidence via caller");
connect("prototype", "product", "handoff", "returns semantic findings via caller");
connect("prototype", "architect", "handoff", "returns feasibility via caller");

// Change playbooks and delivery.
connect("feature", "product", "support", "fills behavior gaps");
connect("feature", "how", "support", "grounds existing system");
connect("feature", "solution", "support", "settles overall approach");
connect("feature", "ui-refinement", "support", "runs reviewed UI loop");
connect("feature", "interaction-design", "support", "designs changed interactions");
connect("feature", "architect", "support", "design-only package");
connect("feature", "swarm", "support", "partitions independent slices");
connect("feature", "arena", "support", "compares live alternatives");
connect("feature", "interrogate", "support", "reviews contested result");
connect("feature", "opening-pr", "handoff", "delivers when authorized");

connect("bug-fix", "how", "support", "traces failure path");
connect("bug-fix", "why", "support", "checks regression history");
connect("bug-fix", "probe", "support", "separates causal hypotheses");
connect("bug-fix", "architect", "support", "designs when trigger applies");
connect("bug-fix", "tdd", "support", "pins cheap regression path");
connect("bug-fix", "opening-pr", "handoff", "delivers when authorized");

connect("refactoring", "how", "support", "captures behavior baseline");
connect("refactoring", "figure-it-out", "support", "handles coupled migration");
connect("refactoring", "architect", "support", "designs when trigger applies");
connect("refactoring", "maintainability", "support", "assesses structural improvement");
connect("refactoring", "feature", "handoff", "separates behavior changes");
connect("refactoring", "bug-fix", "handoff", "separates discovered defects");
connect("refactoring", "opening-pr", "handoff", "delivers when authorized");

connect("figure-it-out", "probe", "support", "reduces empirical uncertainty");
connect("figure-it-out", "architect", "support", "settles consequential shape");
connect("figure-it-out", "swarm", "support", "runs independent slices");
connect("figure-it-out", "arena", "support", "compares unresolved alternatives");
connect("figure-it-out", "show-work", "support", "records consequential decisions");
connect("swarm", "arena", "handoff", "routes candidate comparison");

connect("skill-authoring", "reflect", "support", "finds destination and evidence");
connect("skill-authoring", "evaluation", "support", "tests consequential behavior");
connect("skill-authoring", "opening-pr", "handoff", "delivers when authorized");
connect("reflect", "skill-authoring", "handoff", "sends accepted substantive edits");
connect("opening-pr", "interrogate", "support", "reviews consequential change");
connect("work", "show-work", "support", "records substantial work");

// Shared implementation support; the caller retains all phase transitions.
["feature", "bug-fix", "refactoring", "figure-it-out"].forEach((owner) => {
  connect(owner, "implement", "support", "assigns bounded edits and checks");
  connect(owner, "independent-verification", "support", "assigns separate proof worker");
  connect("architect", owner, "handoff", "returns design or revision via caller");
});
connect("implement", "project-records", "handoff", "returns artifact and evidence via caller");
connect("independent-verification", "project-records", "support", "uses project verifier procedure");
connect("independent-verification", "bootstrap-verification", "handoff", "returns missing proof path via caller");
connect("independent-verification", "maintain-verification", "handoff", "returns recipe drift via caller");
connect("independent-verification", "implement", "handoff", "returns correction need via caller");
connect("execution-contract", "independent-verification", "governance", "owns independent dispatch and exceptions");

// Verification lifecycle.
connect("bootstrap-verification", "how", "support", "traces relevant paths");
connect("bootstrap-verification", "why", "support", "checks historical constraints");
connect("bootstrap-verification", "probe", "support", "tests setup unknowns");
connect("bootstrap-verification", "maintain-verification", "handoff", "hands off subsequent drift");
connect("maintain-verification", "bootstrap-verification", "handoff", "returns when no verifier exists");
connect("maintain-verification", "how", "support", "traces unclear flow");

// Durable records and system-wide governance. These are hidden by default where noted in the UI.
connect("product", "project-records", "handoff", "records requirements");
connect("solution", "project-records", "handoff", "records solution decision");
connect("interaction-design", "project-records", "handoff", "records interaction model");
connect("ui-refinement", "project-records", "handoff", "preserves reviewed reference");
connect("architect", "project-records", "handoff", "records design package");
connect("bootstrap-verification", "project-records", "handoff", "records verifier and map");
connect("maintain-verification", "project-records", "handoff", "updates verifier and map");
connect("reflect", "project-records", "handoff", "records accepted learning");
connect("work", "project-records", "handoff", "consolidates canonical evidence");

connect("execution-contract", "work", "governance", "governs delegation, proof and completion");
connect("principles-index", "work", "governance", "routes approved judgments");
connect("principles-index", "preserve-context", "governance", "matches handoff changes");
connect("principles-index", "ui-meaning", "governance", "matches UI structure changes");
connect("execution-contract", "project-records", "governance", "defines evidence retention");

const lanes = [
  { number: "A", title: "DEFINE & DECIDE", x: 280, y: 20, w: 2300, h: 270 },
  { number: "B", title: "EXPLORE & CHALLENGE", x: 280, y: 310, w: 2300, h: 270 },
  { number: "C", title: "CHANGE & DELIVER", x: 280, y: 600, w: 2300, h: 380 },
  { number: "D", title: "VERIFY & EVOLVE", x: 280, y: 1000, w: 2300, h: 270 },
];

const nodeById = new Map(nodes.map((node) => [node.id, node]));
const svg = document.querySelector("#skill-map");
const laneLayer = document.querySelector("#lanes");
const edgeLayer = document.querySelector("#edges");
const edgeLabelLayer = document.querySelector("#edge-labels");
const nodeLayer = document.querySelector("#nodes");
const searchInput = document.querySelector("#search");
const emptySearch = document.querySelector("#empty-search");

let selectedId = "work";
let focusMode = false;
let tracedEdgeIds = new Set();
const fullView = { x: -360, y: 0, w: 3020, h: 1290 };
let view = { ...fullView };
let hoveredId = null;
let panState = null;

function svgElement(name, attributes = {}) {
  const element = document.createElementNS("http://www.w3.org/2000/svg", name);
  Object.entries(attributes).forEach(([key, value]) => element.setAttribute(key, value));
  return element;
}

function renderLanes() {
  lanes.forEach((lane) => {
    const group = svgElement("g", { class: "lane" });
    group.append(svgElement("rect", { x: lane.x, y: lane.y, width: lane.w, height: lane.h }));

    const number = svgElement("text", { x: lane.x + 18, y: lane.y + 28, class: "lane-number" });
    number.textContent = lane.number;
    group.append(number);

    const title = svgElement("text", { x: lane.x + 43, y: lane.y + 27, class: "lane-title" });
    title.textContent = lane.title;
    group.append(title);
    laneLayer.append(group);
  });
}

function anchorPoints(from, to) {
  const sourceCenter = { x: from.x + from.w / 2, y: from.y + from.h / 2 };
  const targetCenter = { x: to.x + to.w / 2, y: to.y + to.h / 2 };
  const dx = targetCenter.x - sourceCenter.x;
  const dy = targetCenter.y - sourceCenter.y;

  if (Math.abs(dx) >= Math.abs(dy) * 0.65) {
    const forward = dx >= 0;
    return {
      start: { x: forward ? from.x + from.w : from.x, y: sourceCenter.y },
      end: { x: forward ? to.x : to.x + to.w, y: targetCenter.y },
      horizontal: true,
      sourceSide: forward ? "right" : "left",
      targetSide: forward ? "left" : "right",
    };
  }

  const downward = dy >= 0;
  return {
    start: { x: sourceCenter.x, y: downward ? from.y + from.h : from.y },
    end: { x: targetCenter.x, y: downward ? to.y : to.y + to.h },
    horizontal: false,
    sourceSide: downward ? "bottom" : "top",
    targetSide: downward ? "top" : "bottom",
  };
}

function pointOnSide(node, side, position, total) {
  const ratio = (position + 1) / (total + 1);
  const inset = 14;

  if (side === "left" || side === "right") {
    return {
      x: side === "right" ? node.x + node.w : node.x,
      y: node.y + inset + ratio * (node.h - inset * 2),
    };
  }

  return {
    x: node.x + inset + ratio * (node.w - inset * 2),
    y: side === "bottom" ? node.y + node.h : node.y,
  };
}

function portForEdge(edge, node, side, role) {
  const isSource = role === "source";
  const candidates = edges
    .filter((candidate) => (isSource ? candidate.from === node.id : candidate.to === node.id))
    .filter((candidate) => {
      const candidateFrom = nodeById.get(candidate.from);
      const candidateTo = nodeById.get(candidate.to);
      const anchors = anchorPoints(candidateFrom, candidateTo);
      return (isSource ? anchors.sourceSide : anchors.targetSide) === side;
    })
    .sort((a, b) => {
      const aOther = nodeById.get(isSource ? a.to : a.from);
      const bOther = nodeById.get(isSource ? b.to : b.from);
      const verticalSide = side === "left" || side === "right";
      const aPosition = verticalSide ? aOther.y + aOther.h / 2 : aOther.x + aOther.w / 2;
      const bPosition = verticalSide ? bOther.y + bOther.h / 2 : bOther.x + bOther.w / 2;
      return aPosition - bPosition || a.id.localeCompare(b.id);
    });

  return pointOnSide(node, side, candidates.findIndex((candidate) => candidate.id === edge.id), candidates.length);
}

function edgeGeometry(edge) {
  const from = nodeById.get(edge.from);
  const to = nodeById.get(edge.to);
  const { horizontal, sourceSide, targetSide } = anchorPoints(from, to);
  const start = portForEdge(edge, from, sourceSide, "source");
  const end = portForEdge(edge, to, targetSide, "target");
  let path;

  if (horizontal) {
    const bend = Math.max(55, Math.abs(end.x - start.x) * 0.44);
    const direction = end.x >= start.x ? 1 : -1;
    path = `M ${start.x} ${start.y} C ${start.x + bend * direction} ${start.y}, ${end.x - bend * direction} ${end.y}, ${end.x} ${end.y}`;
  } else {
    const bend = Math.max(45, Math.abs(end.y - start.y) * 0.44);
    const direction = end.y >= start.y ? 1 : -1;
    path = `M ${start.x} ${start.y} C ${start.x} ${start.y + bend * direction}, ${end.x} ${end.y - bend * direction}, ${end.x} ${end.y}`;
  }

  return {
    path,
    labelX: (start.x + end.x) / 2,
    labelY: (start.y + end.y) / 2,
  };
}

function renderEdges() {
  edges.forEach((edge) => {
    const geometry = edgeGeometry(edge);
    const path = svgElement("path", {
      d: geometry.path,
      class: `edge ${edge.type}`,
      "data-edge-id": edge.id,
      "data-type": edge.type,
    });
    edgeLayer.append(path);

    const width = Math.max(86, edge.label.length * 7.4 + 22);
    const label = svgElement("g", {
      class: "edge-label",
      "data-edge-id": edge.id,
      "data-type": edge.type,
      transform: `translate(${geometry.labelX - width / 2} ${geometry.labelY - 14})`,
    });
    label.append(svgElement("rect", { width, height: 28, rx: 2 }));
    const text = svgElement("text", { x: width / 2, y: 18, "text-anchor": "middle" });
    text.textContent = edge.label;
    label.append(text);
    edgeLabelLayer.append(label);
  });
}

function wrapWords(value, maxLength) {
  const words = value.split(" ");
  const lines = [];
  let current = "";
  words.forEach((word) => {
    if (!current || `${current} ${word}`.length <= maxLength) {
      current = current ? `${current} ${word}` : word;
    } else {
      lines.push(current);
      current = word;
    }
  });
  if (current) lines.push(current);
  return lines.slice(0, 2);
}

function renderNodes() {
  nodes.forEach((node) => {
    const group = svgElement("g", {
      class: `node ${node.type} ${node.id === "work" ? "work" : ""}`,
      transform: `translate(${node.x} ${node.y})`,
      "data-node-id": node.id,
      tabindex: "0",
      role: "button",
      "aria-label": `${node.title}. ${node.purpose}`,
    });

    group.append(svgElement("rect", {
      class: "node-surface",
      width: node.w,
      height: node.h,
      rx: node.id === "work" ? 4 : 2,
    }));
    group.append(svgElement("rect", { class: "node-accent", width: 6, height: node.h }));

    const type = svgElement("text", { class: "node-type", x: 20, y: 21 });
    type.textContent = TYPE_LABELS[node.type].toUpperCase();
    group.append(type);

    const titleLines = wrapWords(node.title, node.w > 240 ? 27 : 22);
    const title = svgElement("text", { class: "node-title", x: 20, y: node.id === "work" ? 58 : 49 });
    titleLines.forEach((line, index) => {
      const tspan = svgElement("tspan", { x: 20, dy: index === 0 ? 0 : 18 });
      tspan.textContent = line;
      title.append(tspan);
    });
    group.append(title);

    const subtitle = svgElement("text", {
      class: "node-subtitle",
      x: 20,
      y: titleLines.length > 1 ? 88 : node.id === "work" ? 91 : 79,
    });
    subtitle.textContent = node.subtitle;
    group.append(subtitle);

    group.addEventListener("click", () => selectNode(node.id, true));
    group.addEventListener("mouseenter", () => {
      hoveredId = node.id;
      updateGraphState();
    });
    group.addEventListener("mouseleave", () => {
      hoveredId = null;
      updateGraphState();
    });
    group.addEventListener("focus", () => {
      hoveredId = node.id;
      updateGraphState();
    });
    group.addEventListener("blur", () => {
      hoveredId = null;
      updateGraphState();
    });
    group.addEventListener("keydown", (event) => {
      if (event.key === "Enter" || event.key === " ") {
        event.preventDefault();
        selectNode(node.id, true);
      }
    });
    nodeLayer.append(group);
  });
}

function enabledTypes() {
  return new Set(
    [...document.querySelectorAll('.filter input[type="checkbox"]')]
      .filter((input) => input.checked)
      .map((input) => input.value),
  );
}

function relatedNodeIds(id) {
  const ids = new Set([id]);
  edges.forEach((edge) => {
    if (edge.from === id) ids.add(edge.to);
    if (edge.to === id) ids.add(edge.from);
  });
  return ids;
}

function updateGraphState() {
  const allowed = enabledTypes();
  const emphasisId = hoveredId || (focusMode ? selectedId : null);
  const related = emphasisId ? relatedNodeIds(emphasisId) : new Set(nodes.map((node) => node.id));
  const tracedNodeIds = new Set(["work", selectedId]);
  const activeEdgeIds = [];
  edges.forEach((edge) => {
    if (tracedEdgeIds.has(edge.id)) {
      tracedNodeIds.add(edge.from);
      tracedNodeIds.add(edge.to);
    }
  });

  document.querySelectorAll(".node").forEach((element) => {
    const id = element.dataset.nodeId;
    const traceMuted = tracedEdgeIds.size > 0 && !tracedNodeIds.has(id);
    element.classList.toggle("is-selected", id === selectedId);
    element.classList.toggle("is-muted", traceMuted || (Boolean(emphasisId) && !related.has(id)));
  });

  document.querySelectorAll(".edge, .edge-label").forEach((element) => {
    const edge = edges.find((candidate) => candidate.id === element.dataset.edgeId);
    const isAllowed = allowed.has(edge.type);
    const isDirect = emphasisId && (edge.from === emphasisId || edge.to === emphasisId);
    const isTraced = tracedEdgeIds.has(edge.id);
    const isLabel = element.classList.contains("edge-label");
    const isActive = isTraced || (isDirect && !isLabel);
    element.classList.toggle("is-hidden", !isAllowed);
    element.classList.toggle("is-active", isAllowed && isActive);
    element.classList.toggle(
      "is-muted",
      isAllowed && ((tracedEdgeIds.size > 0 && !isTraced) || (Boolean(emphasisId) && !isDirect)),
    );
    if (!isLabel && isAllowed && isActive) activeEdgeIds.push(edge.id);
  });

  // SVG uses document order for painting. Promote focused paths so background
  // relationships cannot visually cut through them at crossings.
  [...new Set(activeEdgeIds)].forEach((edgeId) => {
    const path = edgeLayer.querySelector(`[data-edge-id="${edgeId}"]`);
    if (path) edgeLayer.append(path);
  });

  document.querySelector("#edge-count").textContent = edges.filter((edge) => allowed.has(edge.type)).length;
}

function relationshipButton(edge, direction) {
  const targetId = direction === "out" ? edge.to : edge.from;
  const target = nodeById.get(targetId);
  const button = document.createElement("button");
  button.className = "relationship-item";
  button.type = "button";
  button.innerHTML = `
    <span class="relationship-dot ${edge.type}"></span>
    <span><strong>${target.title}</strong><small>${edge.label}</small></span>
  `;
  button.addEventListener("click", () => selectNode(targetId, true));
  return button;
}

function populateRelationshipList(container, relationships, direction) {
  container.replaceChildren();
  container.scrollTop = 0;
  if (!relationships.length) {
    const empty = document.createElement("p");
    empty.className = "relationship-empty";
    empty.textContent = "No explicit relationships in this direction.";
    container.append(empty);
    return;
  }
  relationships
    .sort((a, b) => nodeById.get(direction === "out" ? a.to : a.from).title.localeCompare(
      nodeById.get(direction === "out" ? b.to : b.from).title,
    ))
    .forEach((edge) => container.append(relationshipButton(edge, direction)));
}

function updateInspector(node) {
  const outgoing = edges.filter((edge) => edge.from === node.id);
  const incoming = edges.filter((edge) => edge.to === node.id);
  document.querySelector("#inspector-kind").textContent = TYPE_LABELS[node.type];
  document.querySelector("#inspector-title").textContent = node.title;
  document.querySelector("#inspector-purpose").textContent = node.purpose;
  document.querySelector("#inspector-owns").textContent = node.owns;
  document.querySelector("#outgoing-count").textContent = outgoing.length;
  document.querySelector("#incoming-count").textContent = incoming.length;
  populateRelationshipList(document.querySelector("#outgoing-list"), outgoing, "out");
  populateRelationshipList(document.querySelector("#incoming-list"), incoming, "in");
  document.querySelector("#source-link").href = node.source;
}

function selectNode(id, enableFocus = false) {
  const node = nodeById.get(id);
  if (!node) return;
  selectedId = id;
  focusMode = enableFocus;
  tracedEdgeIds = new Set();
  updateInspector(node);
  updateGraphState();
  history.replaceState(null, "", `#${id}`);
}

function findPath(fromId, toId) {
  if (fromId === toId) return [];
  const queue = [fromId];
  const visited = new Set([fromId]);
  const previous = new Map();

  while (queue.length) {
    const current = queue.shift();
    for (const edge of edges.filter((candidate) => candidate.from === current)) {
      if (visited.has(edge.to)) continue;
      visited.add(edge.to);
      previous.set(edge.to, edge);
      if (edge.to === toId) {
        const path = [];
        let cursor = toId;
        while (cursor !== fromId) {
          const step = previous.get(cursor);
          path.unshift(step);
          cursor = step.from;
        }
        return path;
      }
      queue.push(edge.to);
    }
  }
  return null;
}

function traceFromWork() {
  const path = findPath("work", selectedId);
  if (path === null) {
    document.querySelector("#trace-button").textContent = "No directed path";
    window.setTimeout(() => {
      document.querySelector("#trace-button").textContent = "Trace from aapilot";
    }, 1400);
    return;
  }

  path.forEach((edge) => {
    const checkbox = document.querySelector(`.filter input[value="${edge.type}"]`);
    if (checkbox) checkbox.checked = true;
  });
  tracedEdgeIds = new Set(path.map((edge) => edge.id));
  focusMode = false;
  updateGraphState();
  fitNodes(["work", ...path.map((edge) => edge.to)]);
}

function showAll() {
  focusMode = false;
  tracedEdgeIds = new Set();
  searchInput.value = "";
  emptySearch.hidden = true;
  document.querySelectorAll(".node").forEach((node) => node.classList.remove("is-match"));
  updateGraphState();
}

function toggleInspector() {
  const workspace = document.querySelector(".workspace");
  const inspector = document.querySelector("#inspector");
  const button = document.querySelector("#inspector-toggle");
  const isOpen = button.getAttribute("aria-expanded") === "true";

  button.setAttribute("aria-expanded", String(!isOpen));
  button.textContent = isOpen ? "Show details" : "Hide details";
  inspector.hidden = isOpen;
  workspace.classList.toggle("inspector-collapsed", isOpen);
}

function setViewBox() {
  svg.setAttribute("viewBox", `${view.x} ${view.y} ${view.w} ${view.h}`);
}

function fitMap() {
  view = { ...fullView };
  setViewBox();
}

function fitNodes(ids) {
  const visibleNodes = [...new Set(ids)].map((id) => nodeById.get(id)).filter(Boolean);
  if (!visibleNodes.length) return;

  const left = Math.min(...visibleNodes.map((node) => node.x));
  const right = Math.max(...visibleNodes.map((node) => node.x + node.w));
  const top = Math.min(...visibleNodes.map((node) => node.y));
  const bottom = Math.max(...visibleNodes.map((node) => node.y + node.h));
  const frame = svg.getBoundingClientRect();
  const aspect = frame.width / frame.height;
  let width = Math.max(720, right - left + 300);
  let height = Math.max(420, bottom - top + 240);

  if (width / height < aspect) width = height * aspect;
  else height = width / aspect;

  view = {
    x: (left + right) / 2 - width / 2,
    y: (top + bottom) / 2 - height / 2,
    w: width,
    h: height,
  };
  setViewBox();
}

function zoomMap(scale) {
  const selectedNode = nodeById.get(selectedId);
  const zoomingInOnSelection = scale < 1 && selectedNode;
  const focusX = zoomingInOnSelection ? selectedNode.x + selectedNode.w / 2 : view.x + view.w / 2;
  const focusY = zoomingInOnSelection ? selectedNode.y + selectedNode.h / 2 : view.y + view.h / 2;
  const nextWidth = Math.min(3000, Math.max(520, view.w * scale));
  const actualScale = nextWidth / view.w;
  const nextHeight = view.h * actualScale;
  view = {
    x: focusX - nextWidth * (zoomingInOnSelection ? 0.22 : 0.5),
    y: focusY - nextHeight / 2,
    w: nextWidth,
    h: nextHeight,
  };
  setViewBox();
}

function clientToSvg(clientX, clientY) {
  const rect = svg.getBoundingClientRect();
  return {
    x: view.x + ((clientX - rect.left) / rect.width) * view.w,
    y: view.y + ((clientY - rect.top) / rect.height) * view.h,
  };
}

function handleSearch() {
  const query = searchInput.value.trim().toLowerCase();
  let matchCount = 0;
  document.querySelectorAll(".node").forEach((element) => {
    const node = nodeById.get(element.dataset.nodeId);
    const haystack = `${node.title} ${node.subtitle} ${node.purpose}`.toLowerCase();
    const matches = query && haystack.includes(query);
    if (matches) matchCount += 1;
    element.classList.toggle("is-match", matches);
    element.classList.toggle("is-muted", Boolean(query) && !matches);
  });
  emptySearch.hidden = !query || matchCount > 0;
}

document.querySelector(".grid-fill").setAttribute("height", fullView.h);

renderLanes();
renderEdges();
renderNodes();

document.querySelector("#skill-count").textContent = nodes.filter((node) =>
  ["work", "skill", "principle"].includes(node.type),
).length;
document.querySelector("#playbook-count").textContent = nodes.filter((node) => node.type === "playbook").length;

document.querySelectorAll('.filter input[type="checkbox"]').forEach((input) => {
  input.addEventListener("change", updateGraphState);
});
document.querySelector("#trace-button").addEventListener("click", traceFromWork);
document.querySelector("#show-all-button").addEventListener("click", showAll);
document.querySelector("#inspector-toggle").addEventListener("click", toggleInspector);
document.querySelector("#fit-button").addEventListener("click", fitMap);
document.querySelector("#zoom-out-button").addEventListener("click", () => zoomMap(1.18));
document.querySelector("#zoom-in-button").addEventListener("click", () => zoomMap(0.84));
searchInput.addEventListener("input", handleSearch);
searchInput.addEventListener("keydown", (event) => {
  if (event.key === "Enter") {
    const match = nodes.find((node) => {
      const haystack = `${node.title} ${node.subtitle} ${node.purpose}`.toLowerCase();
      return haystack.includes(searchInput.value.trim().toLowerCase());
    });
    if (match) selectNode(match.id, true);
  }
});

document.addEventListener("keydown", (event) => {
  if (event.key === "/" && document.activeElement !== searchInput) {
    event.preventDefault();
    searchInput.focus();
  }
  if (event.key === "Escape") showAll();
});

document.querySelector("#copy-link").addEventListener("click", async (event) => {
  const url = window.location.href;
  try {
    await navigator.clipboard.writeText(url);
  } catch {
    const textarea = document.createElement("textarea");
    textarea.value = url;
    textarea.style.position = "fixed";
    textarea.style.opacity = "0";
    document.body.append(textarea);
    textarea.select();
    document.execCommand("copy");
    textarea.remove();
  }
  event.currentTarget.textContent = "Copied";
  window.setTimeout(() => {
    event.currentTarget.textContent = "Copy node link";
  }, 1200);
});

svg.addEventListener("wheel", (event) => {
  event.preventDefault();
  const point = clientToSvg(event.clientX, event.clientY);
  const scale = event.deltaY > 0 ? 1.12 : 0.88;
  const nextWidth = Math.min(3200, Math.max(520, view.w * scale));
  const actualScale = nextWidth / view.w;
  const nextHeight = view.h * actualScale;
  view = {
    x: point.x - (point.x - view.x) * actualScale,
    y: point.y - (point.y - view.y) * actualScale,
    w: nextWidth,
    h: nextHeight,
  };
  setViewBox();
}, { passive: false });

svg.addEventListener("pointerdown", (event) => {
  if (event.target.closest(".node")) return;
  svg.setPointerCapture(event.pointerId);
  panState = { pointerId: event.pointerId, start: clientToSvg(event.clientX, event.clientY), view: { ...view } };
  svg.classList.add("is-panning");
});

svg.addEventListener("pointermove", (event) => {
  if (!panState || panState.pointerId !== event.pointerId) return;
  const current = clientToSvg(event.clientX, event.clientY);
  view.x = panState.view.x + panState.start.x - current.x;
  view.y = panState.view.y + panState.start.y - current.y;
  setViewBox();
});

function endPan(event) {
  if (!panState || panState.pointerId !== event.pointerId) return;
  panState = null;
  svg.classList.remove("is-panning");
}

svg.addEventListener("pointerup", endPan);
svg.addEventListener("pointercancel", endPan);

const initialId = window.location.hash.slice(1);
if (nodeById.has(initialId)) {
  selectNode(initialId, false);
} else {
  updateInspector(nodeById.get("work"));
  updateGraphState();
}
setViewBox();
