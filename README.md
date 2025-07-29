# HRHelper - Employee FAQ Chatbot

## Description
HRHelper is a simple chatbot that answers common HR questions through a web UI and Slack integration.

## Features
- Matches user queries with closest known FAQs
- Simple Flask backend
- Logs unknown queries
- Web and Slack interfaces

## Setup
```bash
pip install flask
python app.py
```
Access the app at `http://localhost:5000/`

## Slack Integration
- Create a Slack App
- Enable Event Subscriptions and point to `/chat`
- Allow `app_mention` event

## Files
- `faq_data.json` - Static Q&A
- `app.py` - API backend
- `index.html` - Web UI
- `style.css` - Styling for web UI
- `unknown.log` - Logs unrecognized questions

## Logging
Unknown queries are stored in `logs/unknown.log`

# ------------------------
# File: prompt_log.md
# ------------------------
**Tried prompt:**
"How many vacation days do I have?"
**Bot reply:**
"Employees are entitled to 20 days of paid leave per year."

**Tried prompt:**
"Where's HR located?"
**Bot reply:**
"It is on the 2nd floor, Room 204."

