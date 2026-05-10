# database.py
# This file does two things:
# 1. Creates our SQLite database and FAQ table (if they don't exist)
# 2. Provides functions to add, read, update, delete FAQs (CRUD)

import sqlite3  # Built into Python — no installation needed
import os       # For building file paths that work on any OS

# --- Configuration ---
# Build the path to our database file dynamically
# __file__ = this file's location (app/database.py)
# os.path.dirname() = gets the folder containing this file (app/)
# os.path.join() = joins path pieces together correctly for any OS
DB_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'edubot.db')


def get_connection():
    """
    Opens a connection to the SQLite database.
    Think of this like opening the FAQ binder.
    SQLite creates the file automatically if it doesn't exist.
    """
    conn = sqlite3.connect(DB_PATH)
    # Row factory makes results return as dictionaries (column_name: value)
    # instead of plain tuples — much easier to work with
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    """
    Creates the 'faqs' table if it doesn't exist yet.
    This is like drawing the columns in our FAQ binder.
    """
    conn = get_connection()
    cursor = conn.cursor()  # Cursor = the pen that writes/reads to the DB

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS faqs (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            question TEXT NOT NULL,
            answer   TEXT NOT NULL
        )
    ''')
    # id       → unique number for each FAQ (auto-assigned by SQLite)
    # category → e.g. "Fees", "Hostel", "Library"
    # question → the FAQ question text
    # answer   → the FAQ answer text

    conn.commit()   # Save the changes (like hitting Ctrl+S)
    conn.close()    # Close the binder when done


def insert_faq(category, question, answer):
    """
    Adds one FAQ entry to the database.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'INSERT INTO faqs (category, question, answer) VALUES (?, ?, ?)',
        (category, question, answer)
        # The ? placeholders prevent SQL injection attacks
        # Never use f-strings or .format() to build SQL queries
    )

    conn.commit()
    conn.close()


def get_all_faqs():
    """
    Returns all FAQ rows from the database as a list.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM faqs')
    rows = cursor.fetchall()  # Fetch every row

    conn.close()
    return rows


def delete_faq(faq_id):
    """
    Deletes a single FAQ by its ID number.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute('DELETE FROM faqs WHERE id = ?', (faq_id,))

    conn.commit()
    conn.close()


def update_faq(faq_id, category, question, answer):
    """
    Updates an existing FAQ's content.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        'UPDATE faqs SET category=?, question=?, answer=? WHERE id=?',
        (category, question, answer, faq_id)
    )

    conn.commit()
    conn.close()
def get_all_faqs_as_list():
    """
    Returns all FAQs as a list of dictionaries.
    Regular get_all_faqs() returns sqlite3.Row objects.
    This version returns plain dicts — easier to work with everywhere.
    """
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM faqs')
    rows = cursor.fetchall()
    conn.close()
    # Convert each sqlite3.Row to a plain dictionary
    return [dict(row) for row in rows]    
