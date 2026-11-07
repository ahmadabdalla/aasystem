"""Synthetic function-level service; transport, persistence and broker are injected."""

async def accept_reading(payload, save, publish):
    if not payload.get("id") or type(payload.get("value")) not in (int, float):
        return 400, {"error": "id and numeric value are required"}
    await save(payload["id"], {**payload, "state": "Accepted"})
    await publish(payload["id"])
    return 202, {"id": payload["id"], "state": "Accepted"}


async def process_reading(reading_id, load, save):
    reading = await load(reading_id)
    if reading["unit"] not in ("C", "F"):
        await save(reading_id, {**reading, "state": "Rejected", "reason": "Unsupported unit"})
        return
    celsius = reading["value"] if reading["unit"] == "C" else (reading["value"] - 32) * 5 / 9
    await save(reading_id, {**reading, "state": "Processed", "celsius": celsius})


async def get_reading(reading_id, load):
    reading = await load(reading_id)
    return (200, reading) if reading is not None else (404, {"error": "Not found"})
