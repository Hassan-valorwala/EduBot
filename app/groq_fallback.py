# groq_fallback.py
# This file handles the Groq API fallback.
# When TF-IDF confidence is below threshold, this function is called.
# It sends the user's question to Groq's Llama 3.3 70B model
# and returns a smart, context-aware response.

import os                          # To read environment variables
from groq import Groq              # Official Groq Python SDK
from dotenv import load_dotenv     # To load our .env file safely

# Load the .env file so GROQ_API_KEY becomes available as an environment variable
# Without this line, os.environ.get() would return None
load_dotenv()

# Initialize the Groq client using the API key from .env
# This is like logging into the Groq service — done once at startup
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY")
)

# This is the system prompt — the secret instruction that gives Groq its personality
# It tells Groq WHO it is, WHAT it does, and HOW it should behave
SYSTEM_PROMPT = """You are EduBot, a friendly and helpful chatbot assistant for a college.
You help students with questions about college life including:
- Exams and results
- Fee structure and payments
- Hostel and accommodation
- Library and resources
- Scholarships and financial aid
- Attendance and leave policies
- Placements and internships
- General college life and facilities

Guidelines:
- Keep responses concise and clear (3-5 sentences maximum)
- Be friendly and supportive — students may be stressed
- If you don't know specific details, give general helpful guidance
- Always suggest contacting the relevant college office for official confirmation
- Never make up specific numbers, dates, or official policies
- Respond only to college-related questions
- If asked something completely unrelated to college, politely redirect
"""


def get_groq_response(user_question):
    """
    Sends the user's question to Groq and returns an AI-generated response.

    Parameters:
        user_question : str → the original question the user typed

    Returns a dictionary with:
        - 'answer'     : the AI generated response text
        - 'confidence' : always None for Groq (no similarity score)
        - 'source'     : always 'groq' so the UI can label it correctly
    """

    try:
        # Make the API call to Groq
        # This is like sending a message to the AI and waiting for reply
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # The specific AI model we're using
            messages=[
                {
                    "role": "system",        # System role = background instructions
                    "content": SYSTEM_PROMPT # Our college context + behaviour rules
                },
                {
                    "role": "user",          # User role = what the student asked
                    "content": user_question
                }
            ],
            max_tokens=300,    # Limit response length — keeps answers concise
            temperature=0.7,   # Creativity level: 0 = robotic, 1 = very creative
                               # 0.7 = friendly and natural but not random
        )

        # Extract the actual text from the response object
        # The response has a nested structure — we dig into it to get the message
        answer = response.choices[0].message.content

        return {
            'answer': answer,
            'confidence': None,   # Groq doesn't give a confidence score
            'source': 'groq'      # Label so the UI knows this came from AI
        }

    except Exception as e:
        # If anything goes wrong (network error, invalid key, rate limit)
        # we return a safe fallback message instead of crashing
        return {
            'answer': f"I'm sorry, I couldn't process your question right now. Please try again or contact the college office directly. (Error: {str(e)})",
            'confidence': None,
            'source': 'groq'
        }