import streamlit as st
import os
from textblob.exceptions import MissingCorpusError
from utils.text_analysis import (
    extract_text_from_pdf,
    save_text_file,
    load_text_file,
    clean_and_tokenize_text,
    get_sentiment,
    classify_emotions,
    aspect_sentiment_analysis
)

UPLOAD_DIR = "climate_impact_nepal/data/uploads"
TEXT_DIR = "climate_impact_nepal/data/texts"
os.makedirs(UPLOAD_DIR, exist_ok=True)
os.makedirs(TEXT_DIR, exist_ok=True)

def show_text_analysis_ui():
    st.title(" Text Analysis")
    st.markdown("Upload PDF or TXT files related to Nepal climate change to extract and analyze the content.")

    uploaded_file = st.file_uploader("Upload a PDF or .txt file", type=["pdf", "txt"])

    if uploaded_file is not None:
        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        st.success(f"File saved: {uploaded_file.name}")

        if uploaded_file.name.endswith(".pdf"):
            with st.spinner("Extracting text from PDF..."):
                pdf_text = extract_text_from_pdf(uploaded_file)
                if pdf_text:
                    txt_file_path = os.path.join(TEXT_DIR, uploaded_file.name.replace(".pdf", ".txt"))
                    with open(txt_file_path, "w") as txt_file:
                        txt_file.write(pdf_text)
                    st.success("PDF text extracted and saved!")
                else:
                    st.warning("No text found in PDF.")
        elif uploaded_file.name.endswith(".txt"):
            txt_file_path = os.path.join(TEXT_DIR, uploaded_file.name)
            with open(txt_file_path, "w") as f:
                f.write(uploaded_file.getvalue().decode("utf-8"))
            st.success("Text file saved!")

    st.markdown("---")
    st.subheader("\U0001F4C2 Available Text Files for Analysis")
    text_files = [f for f in os.listdir(TEXT_DIR) if f.endswith(".txt")]

    if text_files:
        selected_file = st.selectbox("Select a .txt file to analyze:", text_files)
        file_path = os.path.join(TEXT_DIR, selected_file)

        with open(file_path, "r") as f:
            raw_text = f.read()

        st.markdown("---")
        st.subheader("\U0001F4C4 Raw Text Preview")
        st.text_area("Content Preview", raw_text[:3000], height=250)

        # Sentiment
        sentiment = get_sentiment(raw_text)
        st.subheader("Sentiment Analysis")
        st.write(f"**Polarity** (−1: negative, +1: positive): `{sentiment['polarity']:.2f}`")
        st.write(f"**Subjectivity** (0: objective, 1: subjective): `{sentiment['subjectivity']:.2f}`")

        

        # Emotion
        st.subheader(" Emotion Classification")
        emotions = classify_emotions(raw_text)
        for emo, score in emotions:
            st.write(f"{emo.capitalize()}: {score:.2f}")


        # Aspect Sentiment
        st.subheader("Aspect-Based Sentiment")
        default_aspects = ["temperature", "rainfall", "climate", "government", "Windspeed", "Precipitation", "dust", "warm", "cold", "extreme"]
        aspects = st.multiselect("Select or add aspects:", default_aspects, default=default_aspects[:2])
        if aspects:
            aspect_scores = aspect_sentiment_analysis(raw_text, aspects)
            if isinstance(aspect_scores, dict):
                for asp, val in aspect_scores.items():
                    st.write(f"{asp}: {val:.2f}")
            else:
                st.write("Aspect sentiment analysis failed or returned invalid data.")
    else:
        st.info("No .txt files found. Please upload one to get started.")


