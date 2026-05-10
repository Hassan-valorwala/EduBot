# test_chatbot.py
# Tests the complete hybrid pipeline end to end

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from chatbot import get_response

print("=" * 55)
print("FULL HYBRID PIPELINE TEST")
print("=" * 55)

questions = [
    # These should hit FAQ
    "library timings",
    "fee payment last date",
    "minimum attendance required",
    "when do exams start",

    # These should hit Groq
    "can I change my branch",
    "what is the meaning of life",
    "how do I deal with exam stress",
]

for question in questions:
    result = get_response(question)
    print(f"\nQ : {question}")
    print(f"Source     : {result['source'].upper()}")
    print(f"Confidence : {result['confidence']}%")
    if result['matched_question']:
        print(f"Matched FAQ: {result['matched_question']}")
    print(f"Answer     : {result['answer'][:100]}...")
    print("-" * 55)
    