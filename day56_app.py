import streamlit as st
import pandas as pd
import string
import nltk

from nltk.corpus import stopwords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

nltk.download("stopwords")

df = pd.read_csv("spam.csv", encoding="latin-1")

df = df[['v1', 'v2']]
df.columns = ['label', 'message']

def clean_text(text):
    text = text.lower()

    text = "".join(
        char for char in text
        if char not in string.punctuation
    )

    words = text.split()

    words = [
        word for word in words
        if word not in stopwords.words("english")
    ]

    return " ".join(words)

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

st.set_page_config(page_title="Smart Spam Detector", page_icon="📩")

st.title("📩 Smart Spam Detector")

st.write("Enter an SMS message below to check whether it is **Spam** or **Ham**.")

message = st.text_area("Enter Message")

if st.button("Predict"):

    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        cleaned = clean_text(message)

        vector = vectorizer.transform([cleaned])

        prediction = model.predict(vector)[0]

        if prediction == 1:
            st.error("🚨 Spam Message Detected")
        else:
            st.success("✅ Ham (Not Spam)")