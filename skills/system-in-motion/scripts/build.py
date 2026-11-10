#!/usr/bin/env python3
"""Validate an explanation model and embed it in the offline viewer."""

import argparse
import json
import math
from pathlib import Path
import re
import sys


class ModelError(ValueError):
    pass


def validate(model):
    """Check structural consistency; source truth still requires human/agent review."""
    def fail(path, message):
        raise ModelError(f"{path}: {message}")

    def text(value, path):
        if not isinstance(value, str) or not value.strip():
            fail(path, "expected non-empty plain text")

    def array(value, path, nonempty=False):
        if not isinstance(value, list) or (nonempty and not value):
            fail(path, "expected a non-empty array" if nonempty else "expected an array")
        return value

    def fields(obj, path, names):
        if not isinstance(obj, dict):
            fail(path, "expected an object")
        for name in names:
            text(obj.get(name), f"{path}.{name}")

    def collection(name, nonempty=True):
        items = array(model.get(name), name, nonempty)
        found = {}
        for index, item in enumerate(items):
            path = f"{name}[{index}]"
            fields(item, path, ["id"])
            key = item["id"]
            if not re.fullmatch(r"[a-z][a-z0-9-]*", key):
                fail(path + ".id", "use lowercase letters, digits and hyphens, beginning with a letter")
            if key in found:
                fail(path + ".id", f"duplicate identifier {key!r}")
            found[key] = item
        return found

    def reference(value, known, path):
        if not isinstance(value, str) or value not in known:
            fail(path, f"unresolved reference {value!r}")

    def number(value, path, minimum=0, maximum=10000):
        if type(value) not in (int, float) or not minimum <= value <= maximum or not math.isfinite(value):
            fail(path, f"expected a finite number between {minimum} and {maximum}")
        return value

    def geometry(obj, path, names):
        if not isinstance(obj, dict) or set(obj) != set(names):
            fail(path, "expected only layout fields: " + ", ".join(names))
        return obj

    def refs(value, known, path):
        for key in array(value, path):
            if not isinstance(key, str) or key not in known:
                fail(path, f"unresolved reference {key!r}")
        if len(value) != len(set(value)):
            fail(path, "duplicate references")

    def claim(obj, path):
        status = obj.get("status")
        if status not in ("implemented", "planned", "inferred", "unknown"):
            fail(path + ".status", "use implemented, planned, inferred or unknown")
        refs(obj.get("evidence"), sources, path + ".evidence")
        if status != "unknown" and not obj["evidence"]:
            fail(path + ".evidence", "a claim needs at least one supporting source")
        if status in {"inferred", "unknown"}:
            text(obj.get("note"), path + ".note")

    fields(model, "model", ["title", "summary", "basis"])
    if type(model.get("version")) is not int or model["version"] != 1:
        fail("version", "expected model version 1")
    if model["basis"] not in {"repository", "synthetic"}:
        fail("basis", "use repository or synthetic")
    sources = collection("sources", nonempty=False)
    lanes = collection("lanes")
    components = collection("components")
    edges = collection("edges", nonempty=False)
    scenes = collection("scenes")
    presentation = model.get("presentation", {})
    if not isinstance(presentation, dict):
        fail("presentation", "expected an object")
    profile = presentation.get("profile", "technical")
    if profile not in ("technical", "business-workflow"):
        fail("presentation.profile", "use technical or business-workflow")
    business = profile == "business-workflow"
    if business:
        canvas = geometry(presentation.get("canvas"), "presentation.canvas", ["width", "height"])
        number(canvas["width"], "presentation.canvas.width", 400, 10000)
        number(canvas["height"], "presentation.canvas.height", 200, 10000)
        dimensions = collection("stateDimensions")
        for key, dimension in dimensions.items():
            fields(dimension, f"stateDimensions.{key}", ["label"])
    for name in ["name", "mark"]:
        if name in presentation:
            text(presentation[name], "presentation." + name)
    if "navigation" in presentation:
        for index, label in enumerate(array(presentation["navigation"], "presentation.navigation")):
            text(label, f"presentation.navigation[{index}]")
        if len(presentation["navigation"]) != len(set(presentation["navigation"])):
            fail("presentation.navigation", "navigation labels must be unique")
    if "boundary" in presentation:
        fields(presentation["boundary"], "presentation.boundary", ["label", "detail"])
    if "accent" in presentation and (not isinstance(presentation["accent"], str) or not re.fullmatch(r"#[0-9a-fA-F]{6}", presentation["accent"])):
        fail("presentation.accent", "expected a six-digit hex color")
    for key, source in sources.items():
        fields(source, f"sources.{key}", ["label", "location"])
    for key, lane in lanes.items():
        path = f"lanes.{key}"
        fields(lane, path, ["label", "initiator"])
        if business:
            if lane.get("performer") not in ("human", "software", "external"):
                fail(path + ".performer", "use human, software or external")
            layout = geometry(lane.get("layout"), path + ".layout", ["y", "height"])
            number(layout["y"], path + ".layout.y", 0, canvas["height"])
            number(layout["height"], path + ".layout.height", 60, canvas["height"])
            if layout["y"] + layout["height"] > canvas["height"]:
                fail(path + ".layout", "lane extends beyond the canvas")
    if business:
        intervals = sorted((lane["layout"]["y"], lane["layout"]["y"] + lane["layout"]["height"]) for lane in lanes.values())
        if any(a[1] > b[0] for a, b in zip(intervals, intervals[1:])):
            fail("lanes", "responsibility lanes overlap")
    cells = set()
    for key, node in components.items():
        path = f"components.{key}"
        if business:
            fields(node, path, ["label", "kind", "lane"])
            reference(node["lane"], lanes, path + ".lane")
            if node["kind"] not in ("activity", "decision", "outcome"):
                fail(path + ".kind", "use activity, decision or outcome")
            if node["kind"] == "decision" and not node["label"].rstrip().endswith("?"):
                fail(path + ".label", "a decision needs a complete question")
            if "detail" in node:
                text(node["detail"], path + ".detail")
            if any(key in node for key in ("step", "business", "row", "column", "placement")):
                fail(path, "business navigation uses scene IDs and geometry uses layout only")
            if "scene" in node:
                reference(node["scene"], scenes, path + ".scene")
                if key not in array(scenes[node["scene"]].get("activeComponents"), path + ".scene.activeComponents"):
                    fail(path + ".scene", "the selected scene must include this active component")
            elif node["kind"] != "outcome":
                fail(path + ".scene", "navigable activities and decisions need one scene ID")
            layout = geometry(node.get("layout"), path + ".layout", ["x", "y", "width", "height"])
            number(layout["x"], path + ".layout.x", 0, canvas["width"])
            number(layout["y"], path + ".layout.y", 0, canvas["height"])
            number(layout["width"], path + ".layout.width", 40, canvas["width"])
            number(layout["height"], path + ".layout.height", 30, canvas["height"])
            if layout["x"] + layout["width"] > canvas["width"] or layout["y"] + layout["height"] > canvas["height"]:
                fail(path + ".layout", "node extends beyond the canvas")
            lane_layout = lanes[node["lane"]]["layout"]
            if layout["y"] < lane_layout["y"] or layout["y"] + layout["height"] > lane_layout["y"] + lane_layout["height"]:
                fail(path + ".layout", "node must remain inside its performer lane")
        else:
            fields(node, path, ["label", "technology", "responsibility", "kind", "lane"])
            if node["kind"] not in {"person", "interface", "service", "process", "queue", "store", "external"}:
                fail(path + ".kind", "unsupported component kind")
            if node["lane"] not in lanes:
                fail(path + ".lane", "unresolved lane")
            for coordinate in ["row", "column"]:
                value = node.get(coordinate)
                if type(value) is not int or value < 1:
                    fail(path + "." + coordinate, "expected a positive integer")
            if node["column"] > 6:
                fail(path + ".column", "use up to six columns; split a crowded journey")
            cell = (node["lane"], node["row"], node["column"])
            if cell in cells:
                fail(path, "two components occupy the same lane/row/column")
            cells.add(cell)
            if "placement" in node and node["placement"] not in ("inside", "outside"):
                fail(path + ".placement", "use inside or outside")
            if "icon" in node and node["icon"] not in ("person", "browser", "service", "process", "queue", "store", "message", "external"):
                fail(path + ".icon", "unsupported semantic icon")
            if "step" in node and (type(node["step"]) is not int or not 1 <= node["step"] <= len(scenes)):
                fail(path + ".step", "expected a scene number")
        claim(node, path)
    for key, edge in edges.items():
        path = f"edges.{key}"
        fields(edge, path, ["from", "to", "label", "kind"])
        reference(edge["from"], components, path + ".from")
        reference(edge["to"], components, path + ".to")
        if edge["from"] == edge["to"]:
            fail(path, "represent internal work in scene.behind rather than a self-edge")
        if business:
            if edge["kind"] not in ("sequence", "branch", "prerequisite"):
                fail(path + ".kind", "use sequence, branch or prerequisite")
            if edge["kind"] == "branch":
                text(edge.get("condition"), path + ".condition")
            if "business" in edge:
                fail(path, "business geometry uses layout only")
            layout = geometry(edge.get("layout"), path + ".layout", ["points", "label"])
            points = array(layout["points"], path + ".layout.points", nonempty=True)
            if not 2 <= len(points) <= 100:
                fail(path + ".layout.points", "expected 2-100 route points")
            for index, point in enumerate(points):
                if not isinstance(point, list) or len(point) != 2:
                    fail(path + ".layout.points", "expected [x, y] points")
                number(point[0], path + f".layout.points[{index}].x", 0, canvas["width"])
                number(point[1], path + f".layout.points[{index}].y", 0, canvas["height"])
                if index and (point == points[index - 1] or (point[0] != points[index - 1][0] and point[1] != points[index - 1][1])):
                    fail(path + ".layout.points", "use distinct orthogonal route points")
            label = geometry(layout["label"], path + ".layout.label", ["x", "y"])
            number(label["x"], path + ".layout.label.x", 0, canvas["width"])
            number(label["y"], path + ".layout.label.y", 0, canvas["height"])
        elif edge["kind"] not in ("request", "event", "read", "write", "response", "observe"):
            fail(path + ".kind", "unsupported exchange kind")
        claim(edge, path)
    if business:
        for key, node in components.items():
            if node["kind"] == "decision":
                alternatives = [edge for edge in edges.values() if edge["from"] == key]
                if len(alternatives) < 2 or any(edge["kind"] != "branch" for edge in alternatives):
                    fail(f"components.{key}", "a decision needs at least two labeled branch alternatives")
                conditions = [edge["condition"].strip().casefold() for edge in alternatives]
                if len(conditions) != len(set(conditions)):
                    fail(f"components.{key}", "decision alternatives need distinct conditions")
    for key, scene in scenes.items():
        path = f"scenes.{key}"
        fields(scene, path, ["title", "description", "trigger"])
        if "short" in scene:
            text(scene["short"], path + ".short")
        duration = scene.get("duration")
        if type(duration) not in (int, float) or not 2 <= duration <= 30 or not math.isfinite(duration):
            fail(path + ".duration", "expected 2-30 seconds")
        claim(scene, path)
        refs(scene.get("activeComponents"), components, path + ".activeComponents")
        refs(scene.get("activeEdges"), edges, path + ".activeEdges")
        active = set(scene["activeComponents"])
        for edge_id in scene["activeEdges"]:
            missing = {edges[edge_id]["from"], edges[edge_id]["to"]} - active
            if missing:
                fail(path + ".activeComponents", f"include participants of active exchange {edge_id!r}: {', '.join(sorted(missing))}")
        if business:
            states = scene.get("states")
            if not isinstance(states, dict) or set(states) != set(dimensions):
                fail(path + ".states", "supply every declared state dimension and no unknown dimensions")
            for dimension, value in states.items():
                text(value, path + ".states." + dimension)
            phases = array(scene.get("phases", [{"edges": scene["activeEdges"]}]), path + ".phases", nonempty=True)
            phased_edges = []
            for index, phase in enumerate(phases):
                phase_path = path + f".phases[{index}]"
                geometry(phase, phase_path, ["edges"])
                refs(phase["edges"], edges, phase_path + ".edges")
                if len(phases) > 1 and not phase["edges"]:
                    fail(phase_path + ".edges", "ordered phases must contain an active relationship")
                phased_edges.extend(phase["edges"])
            if len(phased_edges) != len(set(phased_edges)) or set(phased_edges) != set(scene["activeEdges"]):
                fail(path + ".phases", "phases must contain each active relationship exactly once")
        experience = scene.get("experience")
        fields(experience, path + ".experience", ["actor", "surface", "layout", "state", "title", "body"])
        if experience["layout"] not in {"message", "pipeline", "workbench", "review", "dispatch", "register", "list", "record", "terminal"}:
            fail(path + ".experience.layout", "unsupported experience layout")
        if experience.get("mode", "observed") not in ("observed", "explanation"):
            fail(path + ".experience.mode", "use observed or explanation")
        for name in ["nav", "packet"]:
            if name in experience:
                text(experience[name], path + ".experience." + name)
        for name, required in [("items", "title"), ("stages", "label"), ("audit", "label")]:
            for index, item in enumerate(array(experience.get(name, []), path + ".experience." + name)):
                item_path = f"{path}.experience.{name}[{index}]"
                fields(item, item_path, [required])
                for optional in ["detail", "state"]:
                    if optional in item:
                        text(item[optional], item_path + "." + optional)
        columns = array(experience.get("columns", []), path + ".experience.columns")
        for label in columns:
            text(label, path + ".experience.columns")
        for row in array(experience.get("rows", []), path + ".experience.rows"):
            if not columns or len(array(row, path + ".experience.rows[]")) != len(columns):
                fail(path + ".experience.rows", "row width must match the non-empty columns")
            for value in row:
                text(value, path + ".experience.rows[]")
        for index, field in enumerate(array(experience.get("fields", []), path + ".experience.fields")):
            fields(field, f"{path}.experience.fields[{index}]", ["label", "value"])
        for index, action in enumerate(array(experience.get("actions", []), path + ".experience.actions")):
            text(action, f"{path}.experience.actions[{index}]")
        for index, item in enumerate(array(scene.get("behind"), path + ".behind")):
            fields(item, f"{path}.behind[{index}]", ["component", "action"])
            reference(item["component"], components, path + ".behind")
            if item["component"] not in active:
                fail(path + ".activeComponents", "include the component doing current backstage work")
    return model


def load_model(path):
    if path.stat().st_size > 1_000_000:
        raise ModelError("model exceeds 1 MB; keep this explanation bounded")
    def reject_constant(value):
        raise ModelError(f"non-finite JSON number {value!r}")

    try:
        model = json.loads(path.read_text(encoding="utf-8"), parse_constant=reject_constant)
    except (json.JSONDecodeError, UnicodeDecodeError) as error:
        raise ModelError(f"invalid UTF-8 JSON: {error}") from error
    return validate(model)


def render(model, template):
    marker = "__SYSTEM_IN_MOTION_MODEL__"
    if template.count(marker) != 1:
        raise ModelError("template must contain exactly one model placeholder")
    payload = json.dumps(model, ensure_ascii=False, separators=(",", ":"))
    for character, replacement in [("<", "\\u003c"), ("&", "\\u0026"), ("\u2028", "\\u2028"), ("\u2029", "\\u2029")]:
        payload = payload.replace(character, replacement)
    return template.replace(marker, payload)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("model", type=Path)
    parser.add_argument("--output", type=Path)
    parser.add_argument("--template", type=Path, default=Path(__file__).resolve().parents[1] / "assets" / "viewer.html")
    parser.add_argument("--validate-only", action="store_true")
    args = parser.parse_args()
    if not args.validate_only and args.output is None:
        parser.error("--output is required unless --validate-only is used")
    try:
        model = load_model(args.model)
        if not args.validate_only:
            html = render(model, args.template.read_text(encoding="utf-8"))
            if args.output.resolve() in {args.model.resolve(), args.template.resolve()}:
                raise ModelError("output must not overwrite the model or viewer template")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(html, encoding="utf-8")
            print(f"Built {args.output}")
        print(f"Valid: {len(model['components'])} components, {len(model['edges'])} exchanges, {len(model['scenes'])} scenes")
    except (ModelError, OSError) as error:
        print(f"system-in-motion: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
