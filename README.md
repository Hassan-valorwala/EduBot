---
title: EduBot
emoji: 🎓
colorFrom: pink
colorTo: white
sdk: docker
pinned: false
---
# 🎓 EduBot — College FAQ Chatbot

A hybrid NLP-powered chatbot that answers college-related questions intelligently.
Built as a course assignment project using Python, NLTK, TF-IDF, SQLite, Groq API, and Flask.

---

## 🧠 How It Works

EduBot uses a **two-layer hybrid architecture**:
User Question
│
▼
NLTK Preprocessing
(tokenization → stopword removal → stemming)
│
▼
TF-IDF + Cosine Similarity
(matches against SQLite FAQ database)
│
├── Confidence ≥ 55% → ✅ Return FAQ Answer
│
└── Confidence < 55% → 🤖 Groq API (Llama 3.3 70B) → Return AI Answer
This is how real production chatbots work — fast rule-based matching first,
intelligent AI fallback second.

---

## ✨ Features

- 💬 **Chat UI** — Clean, responsive web interface built with Flask + HTML/CSS/JS
- 🔍 **NLP Matching** — NLTK preprocessing + TF-IDF vectorization + Cosine Similarity
- 🤖 **AI Fallback** — Groq API (Llama 3.3 70B) for questions outside the FAQ database
- 🗄️ **SQLite Database** — 65+ FAQ entries across 8 categories
- 📊 **Confidence Display** — Shows match confidence % for every answer
- 📱 **Fully Responsive** — Works on desktop, tablet, and mobile
- 🔒 **Secure** — API keys managed via python-dotenv, never hardcoded

---

## 🗂️ FAQ Categories

| Category | Examples |
|---|---|
| 📅 Exams & Results | Exam dates, result checking, revaluation |
| 💰 Fees & Payments | Fee structure, deadlines, payment methods |
| 🏠 Hostel | Availability, charges, timings, facilities |
| 📚 Library | Hours, borrowing limits, online journals |
| 🏅 Scholarships | Available scholarships, deadlines, disbursement |
| 📋 Attendance | Minimum requirement, medical leave, condonation |
| 🎓 Placements | Season dates, companies, registration, internships |
| 🏫 General | College hours, bonafide certificate, canteen, sports |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.11 |
| NLP Core | NLTK (tokenization, stemming, stopwords) |
| Matching | Scikit-learn (TF-IDF + Cosine Similarity) |
| Database | SQLite (built-in Python) |
| AI Fallback | Groq API — Llama 3.3 70B |
| Web Framework | Flask |
| Frontend | HTML, CSS, JavaScript |
| Security | python-dotenv |
| Deployment | Hugging Face Spaces |

---

## 📁 Project Structure
EduBot/
├── app/
│   ├── app.py              # Flask web application
│   ├── chatbot.py          # Hybrid pipeline master controller
│   ├── nlp_engine.py       # NLTK preprocessing + TF-IDF matching
│   ├── groq_fallback.py    # Groq API integration
│   ├── database.py         # SQLite CRUD operations
│   └── templates/
│       └── chat.html       # Chat UI (HTML + CSS + JS)
├── data/
│   ├── edubot.db           # SQLite FAQ database
│   ├── seed_faqs.py        # Initial FAQ data (28 entries)
│   └── seed_synonyms.py    # Synonym entries (37 entries)
├── notebooks/
│   ├── test_nlp.py         # NLP engine tests
│   ├── test_groq.py        # Groq fallback tests
│   └── test_chatbot.py     # Full pipeline tests
├── .env                    # API keys (never pushed to GitHub)
├── .gitignore              # Ignores venv, .env, database
├── pyrightconfig.json      # VS Code import path config
├── requirements.txt        # All dependencies
└── README.md               # This file

---

## 🚀 Run Locally

### 1. Clone the repository
```bash
git clone https://github.com/Hassan-valorwala/EduBot.git
cd EduBot
```

### 2. Create virtual environment
```bash
py -3.11 -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the root folder:
Get a free API key at [console.groq.com](https://console.groq.com)

### 5. Set up the database
```bash
python data/seed_faqs.py
python data/seed_synonyms.py
```

### 6. Run the app
```bash
python app/app.py
```

Open your browser at `http://localhost:5000` 🎉

---

## 📸 Screenshots

> Chat UI with FAQ match and confidence display

*(Add screenshots here after deployment)*

---

## 🔮 Future Improvements

- [ ] Admin panel for managing FAQs without code
- [ ] Multi-language support
- [ ] Voice input support
- [ ] Analytics dashboard for most asked questions
- [ ] User feedback system (thumbs up/down per answer)

---

## 👨‍💻 Built By

**Hassan Valorwala**
GitHub → [Hassan-valorwala/EduBot](https://github.com/Hassan-valorwala/EduBot)

---

## 📜 License

This project was built as a college course assignment.