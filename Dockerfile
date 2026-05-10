# Dockerfile
# Tells Hugging Face how to build and run EduBot
# Think of this as a recipe — every line is one instruction

# Start from official Python 3.11 image
# This gives us a clean Linux machine with Python already installed
FROM python:3.11-slim

# Set the working directory inside the container
# All commands from here run inside /app
WORKDIR /app

# Copy requirements first — Docker caches this layer
# So if requirements don't change, it won't reinstall everything
COPY requirements.txt .

# Install all Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Download NLTK data files that our NLP engine needs
# We do this at build time so it's ready when the app starts
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('punkt_tab')"

# Copy all project files into the container
COPY . .

# Run the database seed scripts to populate FAQs
# This creates edubot.db with all 65 FAQ entries at build time
RUN python data/seed_faqs.py
RUN python data/seed_synonyms.py

# Tell Docker this app listens on port 7860
EXPOSE 7860

# The command that starts your app when the container runs
CMD ["python", "app/app.py"]