# test_groq.py
# Tests the Groq API fallback in isolation
# Run from EduBot root folder

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from groq_fallback import get_groq_response

print("=" * 50)
print("TEST: Groq API Fallback")
print("=" * 50)

# These are questions our FAQ database won't answer well
# So they should all go to Groq
test_questions = [
    "Can I change my branch after first year?",
    "What is the meaning of life?",        # Should be redirected politely
    "Is there a gym on campus?",
    "How do I deal with exam stress?",
]

for question in test_questions:
    print(f"\nQuestion: {question}")
    print("-" * 40)
    result = get_groq_response(question)
    print(f"Source  : {result['source'].upper()}")
    print(f"Answer  : {result['answer']}")
    print()