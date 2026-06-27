import pandas as pd
import string
import nltk

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

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

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = MultinomialNB()

model.fit(X_train, y_train)

predictions = model.predict(X_test)

accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", round(accuracy * 100, 2), "%")

print("\nClassification Report\n")
print(classification_report(y_test, predictions))

custom_messages = [
    "Congratulations! You won a free iPhone. Claim now.",
    "Let's meet at the library tomorrow.",
    "Win cash prizes by clicking this link.",
    "Are you coming to class today?"
]

print("\nCustom Predictions\n")

for msg in custom_messages:

    cleaned = clean_text(msg)

    vector = vectorizer.transform([cleaned])

    result = model.predict(vector)[0]

    if result == 1:
        print(f'"{msg}" --> SPAM')
    else:
        print(f'"{msg}" --> HAM')