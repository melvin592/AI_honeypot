from flask import Flask, render_template, request, jsonify
import sys
import json
import mcp_tool
import uuid
import mutimodal
import os
sys.path.insert(0, ".")
import dectector, canary, agent, logger
import minja_detector
import aarf_detector
import alert
import export

app = Flask(__name__)
session_id = str(uuid.uuid4())[:8]
@app.route("/read-emails", methods=["POST"])
def read_emails():
    results = mcp_tool.read_emails(session_id)
    return jsonify({"emails": results})
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    
    # save the file temporarily
    file_path = os.path.join("uploads", file.filename)
    os.makedirs("uploads", exist_ok=True)
    file.save(file_path)
    
    # extract text from file
    extracted_text = mutimodal.extract_text(file_path)
    
    # run through detector
    action = dectector.detect(extracted_text)
    logger.log_event(session_id, "multimodal_" + action)
    
    if action == "normal":
        reply = "File received. No issues found."
    else:
        reply = agent.respond(action)
    
    return jsonify({"reply": reply, "extracted": extracted_text})

@app.route("/")
def home():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])

def chat():
    data = request.get_json()
    user_input = data["message"]

    canary_hit = canary.check_canary(user_input)
    if canary_hit:
        logger.log_event(session_id, "canary_triggered: " + canary_hit)
        return jsonify({"reply": "Access denied."})
    # MINJA detection
    if minja_detector.analyze(session_id, user_input):
        logger.log_event(session_id, "minja_detected")
        print(f"[!] MINJA attack detected - session {session_id}")
    # AARF detection
    if aarf_detector.analyze(user_input):
        logger.log_event(session_id, "aarf_detected")
        print(f"[!] AARF attack detected - session {session_id}")
    

    action = dectector.detect(user_input)
    logger.log_event(session_id, action)
    if action != "normal":
        alert.send_alert(action, session_id, user_input)
    reply = agent.respond(action,user_input)
    return jsonify({"reply": reply})

@app.route("/dashboard")
def dashboard():
    events = []
    total = attacks = canaries = 0

    if os.path.exists("events.json"):
        with open("events.json", "r") as f:
            for line in f:
                event = json.loads(line)
                events.append(event)
                total += 1
                if event["action"] != "normal":
                    attacks += 1
                if "canary" in event["action"]:
                    canaries += 1

    events.reverse()
    return render_template("dashboard.html", events=events, total=total, attacks=attacks, canaries=canaries)

@app.route("/export")
def export_report():
    filename = export.generate_report()
    return jsonify({"message": "Report generated!", "file": filename})
if __name__ == "__main__":
    app.run(debug=True)