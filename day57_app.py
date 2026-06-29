import streamlit as st
import pandas as pd
import string
import nltk
import time

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download("stopwords", quiet=True)

@st.cache_data
def load_data():
    df = pd.read_csv("spam.csv", encoding="latin-1")
    df = df[["v1", "v2"]]
    df.columns = ["label", "message"]
    return df


def clean_text(text):
    text = text.lower()

    text = "".join(
        ch for ch in text
        if ch not in string.punctuation
    )

    words = text.split()

    words = [
        word
        for word in words
        if word not in stopwords.words("english")
    ]

    return " ".join(words)


@st.cache_resource
def train_model():

    df = load_data()

    df["clean_message"] = df["message"].apply(clean_text)

    df["label"] = df["label"].map({
        "ham": 0,
        "spam": 1
    })

    vectorizer = CountVectorizer()

    X = vectorizer.fit_transform(df["clean_message"])

    y = df["label"]

    model = MultinomialNB()

    model.fit(X, y)

    return model, vectorizer


model, vectorizer = train_model()

st.set_page_config(
    page_title="Smart Spam Detector",
    page_icon="📩",
    layout="centered"
)

st.title("📩 Smart Spam Detector")
st.markdown(
    "Predict whether an SMS message is **Spam** or **Ham**."
)

message = st.text_area(
    "Enter your message",
    height=150
)

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:

        start = time.perf_counter()

        cleaned = clean_text(message)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        confidence = model.predict_proba(vector).max() * 100

        end = time.perf_counter()

        prediction_time = (end - start) * 1000

        if prediction == 1:
            st.error("🚨 Spam Message")
        else:
            st.success("✅ Ham (Not Spam)")

        st.progress(confidence / 100)

        st.write(f"**Confidence:** {confidence:.2f}%")

        st.caption(
            f"Prediction completed in {prediction_time:.2f} ms"
        )