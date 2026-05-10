# test_nlp.py
# Quick test to verify our NLP engine works correctly
# Run this from the EduBot root folder

import sys
import os

# Add app folder to path so Python can find our modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from nlp_engine import preprocess, find_best_match
from database import get_all_faqs, create_table

print("=" * 50)
print("TEST 1: Preprocessing")
print("=" * 50)

test_sentences = [
    "When are the end semester exams?",
    "What is the fee payment deadline?",
    "How many books can I borrow from library?",
    "Is hostel accommodation available for students?",
]

for sentence in test_sentences:
    print(f"Original : {sentence}")
    print(f"Processed: {preprocess(sentence)}")
    print()

print("=" * 50)
print("TEST 2: FAQ Matching")
print("=" * 50)

# Load FAQs from database
create_table()
faqs = get_all_faqs()
print(f"Loaded {len(faqs)} FAQs from database\n")

# Test questions — some close matches, some that should fall to Groq
test_questions = [
    "when do exams start",                    # Should match exam FAQ
    "how much is the hostel fee",             # Should match hostel fee FAQ
    "can i get scholarship",                  # Should match scholarship FAQ
    "what is the meaning of life",            # Should NOT match — Groq fallback
    "library timings",                        # Short query — should still match
    "fee payment last date",                  # Different wording — should match
]

for question in test_questions:
    result = find_best_match(question, faqs)
    print(f"Question  : {question}")
    print(f"Source    : {result['source'].upper()}")
    print(f"Confidence: {result['confidence']}%")
    if result['source'] == 'faq':
        print(f"Matched Q : {result['matched_question']}")
        print(f"Answer    : {result['answer'][:80]}...")  # First 80 chars only
    else:
        print(f"→ No FAQ match. Would go to Groq.")
    print()