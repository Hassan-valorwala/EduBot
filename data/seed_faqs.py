# seed_faqs.py
# Run this ONCE to populate the database with initial FAQs
# Think of this like filling out the FAQ binder for the first time

import sys
import os

# Add the app folder to Python's search path so we can import database.py
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'app'))
from database import create_table, insert_faq

def seed_database():
    print("Creating table...")
    create_table()
    print("Table ready.")

    faqs = [
        # Format: (category, question, answer)

        # --- Exams and Results ---
        ("Exams", "When are the end semester exams?",
         "End semester exams are typically held in November (odd semester) and April (even semester). Check the academic calendar on the college website for exact dates."),

        ("Exams", "How can I check my exam results?",
         "Results are published on the college ERP portal. Login with your student ID and navigate to Academics > Results."),

        ("Exams", "What is the passing mark for subjects?",
         "You need a minimum of 40% in theory and 50% in practicals to pass each subject. Overall aggregate must be above 40%."),

        ("Exams", "Can I apply for revaluation of answer sheets?",
         "Yes. Revaluation applications must be submitted within 10 days of result declaration. A fee of Rs. 500 per subject applies."),

        # --- Fee Structure ---
        ("Fees", "What is the annual tuition fee?",
         "Tuition fees vary by programme. B.Tech: Rs. 1,20,000/year, MBA: Rs. 95,000/year, B.Sc: Rs. 45,000/year. Check the fee structure document on the website."),

        ("Fees", "What is the fee payment deadline?",
         "Semester fees must be paid within the first 15 days of each semester. Late payment attracts a fine of Rs. 50 per day."),

        ("Fees", "What payment methods are accepted for fees?",
         "Fees can be paid online via Net Banking, UPI, or Credit/Debit card through the college ERP portal. Cash payments are accepted at the accounts office."),

        ("Fees", "Is there any instalment facility for fee payment?",
         "Yes. Students can request a two-instalment plan from the accounts office before the semester begins. Supporting documents may be required."),

        # --- Hostel ---
        ("Hostel", "Is hostel accommodation available?",
         "Yes. Separate hostels are available for male and female students. Total capacity is 800 students. Apply through the admission office."),

        ("Hostel", "What is the hostel fee?",
         "Hostel fee is Rs. 60,000/year including mess charges. AC rooms are available at Rs. 85,000/year."),

        ("Hostel", "What are the hostel timings?",
         "Hostel gates close at 10:00 PM for all students. Outpass must be collected from the warden for overnight stays outside."),

        ("Hostel", "What facilities are available in the hostel?",
         "Hostel facilities include Wi-Fi, 24-hour water supply, laundry, common room with TV, study hall, and indoor games room."),

        # --- Library ---
        ("Library", "What are the library working hours?",
         "The library is open Monday to Saturday, 8:00 AM to 8:00 PM. On Sundays and holidays, it is open 10:00 AM to 4:00 PM."),

        ("Library", "How many books can I borrow at a time?",
         "Undergraduate students can borrow 3 books for 14 days. Postgraduate students can borrow 5 books for 21 days. Faculty can borrow 10 books for 30 days."),

        ("Library", "How do I access online journals and resources?",
         "The college subscribes to IEEE Xplore, Springer, and JSTOR. Access them via the library portal using your student credentials from inside campus or via VPN."),

        # --- Scholarships ---
        ("Scholarships", "What scholarships are available?",
         "Available scholarships include Government merit scholarships, SC/ST fee waivers, sports quota scholarships, and merit-cum-means scholarships. Check the scholarship portal for eligibility."),

        ("Scholarships", "When is the scholarship application deadline?",
         "Scholarship applications open in July each year and must be submitted before September 30. Late applications are not accepted."),

        ("Scholarships", "How is scholarship money disbursed?",
         "Approved scholarship amounts are transferred directly to the student's bank account registered with the college within 60 days of approval."),

        # --- Attendance ---
        ("Attendance", "What is the minimum attendance requirement?",
         "A minimum of 75% attendance is mandatory in each subject to be eligible to appear in end semester examinations."),

        ("Attendance", "What happens if my attendance is below 75%?",
         "Students with attendance below 75% will be detained from exams. A medical or special leave application can be submitted for condonation up to 65%."),

        ("Attendance", "How can I apply for medical leave?",
         "Submit a medical certificate from a registered doctor to your class tutor within 3 days of returning. Leave will be updated in the ERP portal within 5 working days."),

        # --- Placements ---
        ("Placements", "When does campus placement season start?",
         "Campus placement season starts in August for final year students. Pre-placement training begins in June. Register on the placement portal to participate."),

        ("Placements", "What companies have recruited from the college?",
         "Top recruiters include TCS, Infosys, Wipro, Cognizant, Accenture, L&T, and various startups. Average package is Rs. 4.5 LPA, highest is Rs. 18 LPA."),

        ("Placements", "How do I register for campus placements?",
         "Log into the placement portal with your student credentials, complete your profile, upload resume, and register for eligible company drives as they are announced."),

        ("Placements", "Are internship opportunities provided by the college?",
         "Yes. The placement cell shares internship opportunities from May to July each year. Students can also apply independently and get it registered as their official internship."),

        # --- General ---
        ("General", "What are the college working hours?",
         "College is open Monday to Saturday, 8:00 AM to 5:00 PM. Administrative offices are open 9:00 AM to 4:30 PM."),

        ("General", "How do I get a bonafide certificate?",
         "Apply for a bonafide certificate through the ERP portal under Student Services. It will be ready within 3 working days. Collect from the administrative office."),

        ("General", "Is there a canteen on campus?",
         "Yes. The main canteen operates from 7:30 AM to 7:00 PM. A smaller café near the library is open till 9:00 PM on weekdays."),

        ("General", "What sports facilities are available?",
         "The campus has a cricket ground, football field, basketball and volleyball courts, a gymnasium, and an indoor badminton hall. Facilities are open 6:00 AM to 8:00 PM."),
    ]

    print(f"Inserting {len(faqs)} FAQs...")
    for category, question, answer in faqs:
        insert_faq(category, question, answer)

    print(f"✅ Done! {len(faqs)} FAQs successfully added to the database.")

if __name__ == "__main__":
    seed_database()