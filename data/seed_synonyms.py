# seed_synonyms.py
# Adds alternative phrasings of existing FAQ questions
# This solves the vocabulary mismatch problem in TF-IDF
# Run this ONCE after seed_faqs.py

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))

from database import create_table, insert_faq

def seed_synonyms():
    print("Adding synonym FAQ entries...")

    synonyms = [
        # --- Exams ---
        ("Exams", "when do exams start",
         "End semester exams are typically held in November (odd semester) and April (even semester). Check the academic calendar on the college website for exact dates."),

        ("Exams", "what is the exam schedule",
         "End semester exams are typically held in November (odd semester) and April (even semester). Check the academic calendar on the college website for exact dates."),

        ("Exams", "exam dates this semester",
         "End semester exams are typically held in November (odd semester) and April (even semester). Check the academic calendar on the college website for exact dates."),

        ("Exams", "how to check my results",
         "Results are published on the college ERP portal. Login with your student ID and navigate to Academics > Results."),

        ("Exams", "where can i see my marks",
         "Results are published on the college ERP portal. Login with your student ID and navigate to Academics > Results."),

        ("Exams", "minimum marks to pass",
         "You need a minimum of 40% in theory and 50% in practicals to pass each subject. Overall aggregate must be above 40%."),

        ("Exams", "how to apply for revaluation",
         "Revaluation applications must be submitted within 10 days of result declaration. A fee of Rs. 500 per subject applies."),

        # --- Fees ---
        ("Fees", "fee payment last date",
         "Semester fees must be paid within the first 15 days of each semester. Late payment attracts a fine of Rs. 50 per day."),

        ("Fees", "what is the deadline for paying fees",
         "Semester fees must be paid within the first 15 days of each semester. Late payment attracts a fine of Rs. 50 per day."),

        ("Fees", "fee due date",
         "Semester fees must be paid within the first 15 days of each semester. Late payment attracts a fine of Rs. 50 per day."),

        ("Fees", "how much is the college fee",
         "Tuition fees vary by programme. B.Tech: Rs. 1,20,000/year, MBA: Rs. 95,000/year, B.Sc: Rs. 45,000/year."),

        ("Fees", "what are the payment options for fees",
         "Fees can be paid online via Net Banking, UPI, or Credit/Debit card through the college ERP portal. Cash payments are accepted at the accounts office."),

        ("Fees", "can i pay fees in installments",
         "Yes. Students can request a two-instalment plan from the accounts office before the semester begins. Supporting documents may be required."),

        # --- Hostel ---
        ("Hostel", "is hostel available",
         "Yes. Separate hostels are available for male and female students. Total capacity is 800 students. Apply through the admission office."),

        ("Hostel", "hostel charges per year",
         "Hostel fee is Rs. 60,000/year including mess charges. AC rooms are available at Rs. 85,000/year."),

        ("Hostel", "what time does hostel close",
         "Hostel gates close at 10:00 PM for all students. Outpass must be collected from the warden for overnight stays outside."),

        ("Hostel", "hostel facilities",
         "Hostel facilities include Wi-Fi, 24-hour water supply, laundry, common room with TV, study hall, and indoor games room."),

        # --- Library ---
        ("Library", "library timings",
         "The library is open Monday to Saturday, 8:00 AM to 8:00 PM. On Sundays and holidays, it is open 10:00 AM to 4:00 PM."),

        ("Library", "when does library open",
         "The library is open Monday to Saturday, 8:00 AM to 8:00 PM. On Sundays and holidays, it is open 10:00 AM to 4:00 PM."),

        ("Library", "library opening hours",
         "The library is open Monday to Saturday, 8:00 AM to 8:00 PM. On Sundays and holidays, it is open 10:00 AM to 4:00 PM."),

        ("Library", "how many books can i take from library",
         "Undergraduate students can borrow 3 books for 14 days. Postgraduate students can borrow 5 books for 21 days."),

        ("Library", "how to access online journals",
         "The college subscribes to IEEE Xplore, Springer, and JSTOR. Access them via the library portal using your student credentials."),

        # --- Scholarships ---
        ("Scholarships", "can i get scholarship",
         "Available scholarships include Government merit scholarships, SC/ST fee waivers, sports quota scholarships, and merit-cum-means scholarships."),

        ("Scholarships", "scholarship application deadline",
         "Scholarship applications open in July each year and must be submitted before September 30. Late applications are not accepted."),

        ("Scholarships", "when will i get scholarship money",
         "Approved scholarship amounts are transferred directly to the student's bank account within 60 days of approval."),

        # --- Attendance ---
        ("Attendance", "minimum attendance required",
         "A minimum of 75% attendance is mandatory in each subject to be eligible to appear in end semester examinations."),

        ("Attendance", "what happens if attendance is low",
         "Students with attendance below 75% will be detained from exams. Condonation is possible up to 65% with valid reason."),

        ("Attendance", "how to apply for medical leave",
         "Submit a medical certificate from a registered doctor to your class tutor within 3 days of returning."),

        # --- Placements ---
        ("Placements", "when does placement start",
         "Campus placement season starts in August for final year students. Pre-placement training begins in June."),

        ("Placements", "which companies come for placement",
         "Top recruiters include TCS, Infosys, Wipro, Cognizant, Accenture, L&T. Average package is Rs. 4.5 LPA."),

        ("Placements", "how to register for placement",
         "Log into the placement portal, complete your profile, upload resume, and register for eligible company drives."),

        ("Placements", "internship opportunities",
         "The placement cell shares internship opportunities from May to July each year. Students can also apply independently."),

        # --- General ---
        ("General", "college timing",
         "College is open Monday to Saturday, 8:00 AM to 5:00 PM. Administrative offices are open 9:00 AM to 4:30 PM."),

        ("General", "how to get bonafide certificate",
         "Apply through the ERP portal under Student Services. It will be ready within 3 working days."),

        ("General", "canteen timings",
         "The main canteen operates from 7:30 AM to 7:00 PM. A café near the library is open till 9:00 PM on weekdays."),

        ("General", "sports facilities in college",
         "The campus has a cricket ground, football field, basketball and volleyball courts, gymnasium, and badminton hall."),
    ]

    for category, question, answer in synonyms:
        insert_faq(category, question, answer)

    print(f"✅ Done! {len(synonyms)} synonym entries added.")

if __name__ == "__main__":
    create_table()
    seed_synonyms()