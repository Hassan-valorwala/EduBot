# chatbot.py
# This is the master controller of EduBot.
# It connects the NLP engine and Groq fallback into one clean pipeline.
#
# Flow:
# User question
#   → preprocess with NLTK
#   → TF-IDF match against FAQ database
#   → if confidence >= 55% → return FAQ answer
#   → if confidence < 55%  → send to Groq → return AI answer

import sys
import os

# Make sure Python can find our other modules
sys.path.append(os.path.dirname(__file__))

from nlp_engine import find_best_match      # TF-IDF matcher
from groq_fallback import get_groq_response # Groq AI fallback
from database import get_all_faqs           # Load FAQs from SQLite


def get_response(user_question):
    """
    The single entry point for the entire EduBot pipeline.
    Call this function with any user question — it handles everything.

    Parameters:
        user_question : str → raw question typed by the user

    Returns a dictionary with:
        - 'answer'           : the final answer to show the user
        - 'confidence'       : match % (None if Groq was used)
        - 'source'           : 'faq' or 'groq'
        - 'matched_question' : the FAQ that matched (None if Groq was used)
    """

    # Step 1: Basic input validation
    # Strip whitespace from both ends
    user_question = user_question.strip()

    # If user sent empty message, handle gracefully
    if not user_question:
        return {
            'answer': 'Please type a question and I will do my best to help you!',
            'confidence': None,
            'source': 'system',
            'matched_question': None
        }

    # Step 2: Load all FAQs from the database
    # We load fresh every time so admin additions are reflected immediately
    faqs = get_all_faqs()

    # Step 3: Try NLP matching first
    nlp_result = find_best_match(user_question, faqs)

    # Step 4: Decision point
    if nlp_result['source'] == 'faq':
        # NLP found a good match — return it directly
        # No need to call Groq at all — saves time and API calls
        return {
            'answer': nlp_result['answer'],
            'confidence': nlp_result['confidence'],
            'source': 'faq',
            'matched_question': nlp_result['matched_question']
        }
    else:
        # NLP confidence was too low — escalate to Groq
        groq_result = get_groq_response(user_question)
        return {
            'answer': groq_result['answer'],
            'confidence': nlp_result['confidence'], # Show how low the NLP score was
            'source': 'groq',
            'matched_question': None
        }