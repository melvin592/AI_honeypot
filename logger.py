import json
import datetime

# ── Piece 1: Logger ───────────────────────
def log_event(session_id, action):
    time = datetime.datetime.now()
    event = {
        "time": str(time),
        "session": session_id,
        "action": action
    }
    with open("events.json", "a") as f:
        f.write(json.dumps(event) + "\n")