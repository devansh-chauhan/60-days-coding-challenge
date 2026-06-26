import pandas as pd
import string
from nltk.corpus import stopwords
import nltk

nltk.download('stopwords')
df = pd.read_csv("spam.csv", encoding="latin-1")
df = df[['v1', 'v2']]
df.columns = ['label', 'message']

print("First 5 Records:")
print(df.head())

def clean_text(text):
    text = text.lower()
    text = "".join(
        char for char in text
        if char not in string.punctuation
    )

    words = text.split()
    words = [
        word for word in words
        if word not in stopwords.words('english')
    ]

    return " ".join(words)

df["clean_message"] = df["message"].apply(clean_text)

print("\nDataset Shape:", df.shape)
print("\nSpam vs Ham:")
print(df["label"].value_counts())
print("\nSample Cleaned Messages:")
print(df[["label", "clean_message"]].head())