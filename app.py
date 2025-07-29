from flask import Flask, request, jsonify, render_template
import json
import difflib
import os
from datetime import datetime

app = Flask(__name__)

# Load FAQ dataset
with open('faq_data.json') as f:
    faq_data = json.load(f)

# Helper function to find best match
def find_answer(user_message):
    questions = [faq['question'] for faq in faq_data]
    match = difflib.get_close_matches(user_message, questions, n=1, cutoff=0.5)
    if match:
        for faq in faq_data:
            if faq['question'] == match[0]:
                return faq['answer']
    else:
        log_unknown_question(user_message)
        return "Sorry, I don't know the answer to that. We'll get back to you soon."

# Log unknown questions
def log_unknown_question(question):
    os.makedirs('logs', exist_ok=True)
    with open('logs/unknown.log', 'a') as f:
        f.write(f"{datetime.now()}: {question}\n")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    answer = find_answer(user_message)
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
