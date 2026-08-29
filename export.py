from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
import json
import os
import datetime

def generate_report():
    # output path
    filename = f"honeypot_report_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
    
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4
    
    # ── Title ─────────────────────────────
    c.setFont("Helvetica-Bold", 20)
    c.drawString(50, height - 50, "AI Honeypot Threat Report")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 80, f"Generated: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # ── Read events ───────────────────────
    events = []
    total = attacks = canaries = 0
    attack_types = {}
    
    if os.path.exists("events.json"):
        with open("events.json", "r") as f:
            for line in f:
                event = json.loads(line)
                events.append(event)
                total += 1
                if event["action"] != "normal":
                    attacks += 1
                    attack_types[event["action"]] = attack_types.get(event["action"], 0) + 1
                if "canary" in event["action"]:
                    canaries += 1
    
    # ── Summary ───────────────────────────
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 120, "Summary")
    
    c.setFont("Helvetica", 12)
    c.drawString(50, height - 145, f"Total Events  : {total}")
    c.drawString(50, height - 165, f"Total Attacks : {attacks}")
    c.drawString(50, height - 185, f"Canaries      : {canaries}")
    
    # ── Attack breakdown ──────────────────
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, height - 220, "Attack Breakdown")
    
    y = height - 245
    c.setFont("Helvetica", 12)
    for attack, count in attack_types.items():
        c.drawString(50, y, f"{attack}: {count}")
        y -= 20
    
    # ── Event log ─────────────────────────
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y - 20, "Event Log")
    
    y -= 45
    c.setFont("Helvetica", 10)
    for event in events[-20:]:  # last 20 events
        line = f"{event['time'][:19]}  |  {event['session']}  |  {event['action']}"
        c.drawString(50, y, line)
        y -= 18
        if y < 50:  # new page if running out of space
            c.showPage()
            y = height - 50
    
    c.save()
    return filename