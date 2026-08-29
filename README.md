# 🏦 SecureBank Pro - AI Honeypot

A deception-based AI security honeypot disguised as a bank website. Built to detect, log and analyze modern AI attacks in real time.

## 🎯 What it detects
- Prompt Injection (OWASP LLM01)
- Multi-Modal Injection (PDF/Image attacks)
- MCP Tool Poisoning
- MINJA Attack (probing detection)
- AARF - Agentic AI Request Forgery
- Credential Theft (Canary Tokens)
- Memory Poisoning (OWASP LLM04)

## 🛠️ Tech Stack
- Python + Flask
- sentence-transformers (semantic detection)
- PyMuPDF + pytesseract (file analysis)
- ReportLab (PDF export)

## 📁 Project Structure
## 📁 Project Structure

AI_honeypot/
├── app.py ← web server
├── agent.py ← fake bank assistant
├── detector.py ← keyword + semantic detection
├── canary.py ← stolen token detection
├── logger.py ← event logging
├── minja_detector.py ← probing detection
├── aarf_detector.py ← request forgery detection
├── mcp_tool.py ← fake email tool
├── multimodal.py ← PDF + image extraction
├── export.py ← PDF report generator
├── alert.py ← email alerts
└── templates/
├── chat.html ← SecureBank Pro frontend
└── dashboard.html ← attack monitoring

## 🚀 How to run

Visit:
- `http://localhost:5000` → SecureBank Pro (hacker view)
- `http://localhost:5000/dashboard` → Attack Dashboard (your view)

## ⚠️ Disclaimer
This project is for educational and research purposes only.