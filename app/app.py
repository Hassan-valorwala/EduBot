# app.py
# The Flask web application — EduBot's front door.
# Handles two things:
# 1. Serves the chat HTML page when user opens the browser
# 2. Receives questions via POST request and returns answers as JSON

import sys
import os

# Add app folder to path so imports work correctly
sys.path.append(os.path.dirname(__file__))

from flask import Flask, render_template, request, jsonify
# Flask        → the web framework itself
# render_template → loads HTML files from the templates/ folder
# request      → lets us read data sent from the browser
# jsonify      → converts Python dictionaries to JSON responses

from chatbot import get_response  # Our hybrid pipeline master controller

# Initialize the Flask application
# __name__ tells Flask where to look for templates and static files
app = Flask(__name__)


@app.route('/')
def home():
    """
    Route: GET /
    When user opens http://localhost:5000 in browser,
    Flask runs this function and returns the chat page.
    """
    return render_template('chat.html')


@app.route('/chat', methods=['POST'])
def chat():
    """
    Route: POST /chat
    When user sends a message, JavaScript sends it here as JSON.
    We run it through the chatbot pipeline and return the answer as JSON.
    """

    # Get the JSON data sent from the browser
    # request.json contains the parsed JSON body
    data = request.json

    # Extract the question — .get() returns None if key doesn't exist
    user_question = data.get('question', '').strip()

    # Handle empty question gracefully
    if not user_question:
        return jsonify({
            'answer': 'Please type a question first!',
            'source': 'system',
            'confidence': None
        })

    # Run through the full hybrid pipeline
    result = get_response(user_question)

    # Return the result as JSON back to the browser
    # jsonify() converts our Python dict to proper JSON format
    return jsonify({
        'answer': result['answer'],
        'source': result['source'],           # 'faq' or 'groq'
        'confidence': result['confidence'],   # percentage or None
        'matched_question': result.get('matched_question')
    })


if __name__ == '__main__':
    # debug=True means:
    # 1. Auto-restarts server when you save code changes
    # 2. Shows detailed error messages in browser
    # NEVER use debug=True in production — only during development
    app.run(debug=True)