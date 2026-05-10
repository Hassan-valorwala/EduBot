# nlp_engine.py
# This is the BRAIN of EduBot.
# It takes a user's raw question, cleans it up using NLP,
# then finds the most similar FAQ from our database using TF-IDF.

import nltk                                      # Main NLP library
from nltk.tokenize import word_tokenize          # Splits sentence into words
from nltk.corpus import stopwords                # List of filler words to remove
from nltk.stem import PorterStemmer             # Cuts words to their root
from sklearn.feature_extraction.text import TfidfVectorizer  # Converts text to numbers
from sklearn.metrics.pairwise import cosine_similarity       # Measures similarity
import numpy as np                               # For finding the highest score

# --- One-time downloads ---
# NLTK needs to download language data files the first time.
# 'punkt' = tokenizer rules, 'stopwords' = list of filler words
# quiet=True means it won't print download logs every time
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)  # Required in newer NLTK versions

# --- Initialize tools ---
stemmer = PorterStemmer()  # Our stemming tool — one instance, reused every time

# Get the English stopwords list from NLTK
# It contains ~179 words like "the", "is", "are", "when", "do", etc.
STOPWORDS = set(stopwords.words('english'))
# We use set() because checking membership in a set is much faster than a list


def preprocess(text):
    """
    Takes a raw sentence and returns a cleaned, stemmed string.

    Example:
        Input:  "When are the end semester Exams held?"
        Output: "end semest exam held"

    Steps:
        1. Lowercase everything
        2. Tokenize (split into words)
        3. Remove stopwords and non-alphabetic tokens (numbers, punctuation)
        4. Stem each word
        5. Join back into a single string (TF-IDF needs strings, not lists)
    """

    # Step 1: Lowercase
    # "Exams" and "exams" must be treated as the same word
    text = text.lower()

    # Step 2: Tokenize
    # word_tokenize splits "when are exams?" into ["when", "are", "exams", "?"]
    tokens = word_tokenize(text)

    # Step 3 + 4: Filter and Stem in one loop
    # isalpha() = True only if the token contains letters only
    # This removes "?", ".", "2024", etc.
    # We also skip the token if it's a stopword
    processed_tokens = [
        stemmer.stem(token)           # Step 4: Stem the word
        for token in tokens           # Loop through every token
        if token.isalpha()            # Step 3a: Keep only alphabetic tokens
        and token not in STOPWORDS    # Step 3b: Remove stopwords
    ]

    # Step 5: Join tokens back into a string
    # TF-IDF vectorizer expects strings, not lists
    # ["exam", "semest", "held"] → "exam semest held"
    return ' '.join(processed_tokens)


def find_best_match(user_question, faqs, threshold=0.55):
    """
    Finds the most similar FAQ to the user's question using TF-IDF + Cosine Similarity.

    Parameters:
        user_question : str  → what the user typed
        faqs          : list → all FAQ rows from the database
        threshold     : float → minimum confidence to count as a match (default 70%)

    Returns a dictionary with:
        - 'answer'     : the FAQ answer (or None if no match)
        - 'confidence' : the similarity score as a percentage
        - 'matched_question' : the FAQ question that matched
        - 'source'     : 'faq' if matched, 'groq' signal if not
    """

    # Edge case: if database is empty, there's nothing to match against
    if not faqs:
        return {'answer': None, 'confidence': 0, 'matched_question': None, 'source': 'groq'}

    # Step 1: Preprocess the user's question
    processed_user_q = preprocess(user_question)

    # Step 2: Preprocess every FAQ question from the database
    # faqs is a list of sqlite3.Row objects — access columns like faqs[i]['question']
    faq_questions = [preprocess(faq['question']) for faq in faqs]

    # Step 3: Build the TF-IDF matrix
    # We combine the user question + all FAQ questions into one list
    # TF-IDF needs to see ALL sentences together to calculate word importance
    all_texts = [processed_user_q] + faq_questions
    # Index 0 = user question
    # Index 1 onwards = FAQ questions

    # TfidfVectorizer converts each sentence into a vector of numbers
    vectorizer = TfidfVectorizer()
    try:
        tfidf_matrix = vectorizer.fit_transform(all_texts)
        # tfidf_matrix shape: (number_of_sentences, number_of_unique_words)
        # Each row = one sentence represented as numbers
    except ValueError:
        # This happens if the user typed something with no meaningful words
        # e.g. "??? !!!" after preprocessing becomes empty string
        return {'answer': None, 'confidence': 0, 'matched_question': None, 'source': 'groq'}

    # Step 4: Calculate Cosine Similarity
    # Compare user question vector (row 0) against all FAQ vectors (rows 1 onwards)
    tfidf_dense = tfidf_matrix.toarray()
    user_vector = tfidf_dense[0].reshape(1, -1)  # Reshape from 1D to 2D — one row, many columns
    faq_vectors = tfidf_dense[1:]                # Already 2D — no change needed    # All FAQ question vectors

    # cosine_similarity returns a 2D array — we flatten it to a 1D list
    similarities = cosine_similarity(user_vector, faq_vectors).flatten()
    # Example: [0.82, 0.14, 0.05, 0.61, ...] — one score per FAQ

    # Step 5: Find the highest similarity score
    best_index = np.argmax(similarities)      # Index of the highest score
    best_score = similarities[best_index]     # The actual score (0.0 to 1.0)

    # Step 6: Convert score to percentage for display
    confidence = round(float(best_score) * 100, 2)  # e.g. 0.82 → 82.0%

    # Step 7: Apply threshold
    # If best match is above 70% confidence → it's a real match
    # If below 70% → the question is too different → fall back to Groq
    if best_score >= threshold:
        matched_faq = faqs[best_index]
        return {
            'answer': matched_faq['answer'],
            'confidence': confidence,
            'matched_question': matched_faq['question'],
            'source': 'faq'       # Tells app.py this came from FAQ database
        }
    else:
        return {
            'answer': None,
            'confidence': confidence,
            'matched_question': None,
            'source': 'groq'      # Tells app.py to use Groq fallback
        }