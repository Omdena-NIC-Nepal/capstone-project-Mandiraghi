import os
import re
import fitz  # PyMuPDF
import spacy
from spacy.cli import download 
from textblob import TextBlob
from collections import Counter
import pandas as pd
import numpy as np
from collections import defaultdict
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")


# Extract full text from a PDF file
def extract_text_from_pdf(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# Save text content to .txt file
def save_text_file(text, filename, save_dir="extracted_texts"):
    os.makedirs(save_dir, exist_ok=True)
    file_path = os.path.join(save_dir, filename)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(text)
    return file_path

# Load and clean plain text from file
def load_text_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

# Clean and tokenize text
def clean_and_tokenize_text(text):
    text = re.sub(r"\s+", " ", text.strip())
    doc = nlp(text)
    tokens = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
    return tokens

# Sentiment analysis using TextBlob
def get_sentiment(text):
    try:
        blob = TextBlob(text)
        return {
            "polarity": blob.sentiment.polarity,
            "subjectivity": blob.sentiment.subjectivity
        }
    except MissingCorpusError:
        return {
            "polarity": None,
            "subjectivity": None
        }


# Emotion detection (rule-based example)
def classify_emotions(text):
    emotion_keywords = {
        "joy": ["happy", "joy", "glad", "delight", "smile"],
        "sadness": ["sad", "unhappy", "depressed", "tear", "grief"],
        "anger": ["angry", "mad", "rage", "furious"],
        "fear": ["fear", "scared", "afraid", "terrified"],
        "surprise": ["surprise", "shocked", "amazed"],
        "disgust": ["disgust", "gross", "nasty"]
    }
    text = text.lower()
    emotion_counter = Counter()
    for emotion, keywords in emotion_keywords.items():
        for word in keywords:
            emotion_counter[emotion] += text.count(word)
    return emotion_counter.most_common(3)


# Sentiment over time (if text chunks have timestamps or meta info)
def sentiment_over_time(texts_with_dates):
    df = pd.DataFrame(texts_with_dates, columns=["date", "text"])
    df["polarity"] = df["text"].apply(lambda x: TextBlob(x).sentiment.polarity)
    df["subjectivity"] = df["text"].apply(lambda x: TextBlob(x).sentiment.subjectivity)
    return df
