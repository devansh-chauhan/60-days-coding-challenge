# Day 55 - Smart Spam Detector (Part 2)

## Problem Statement

Build a machine learning model that automatically classifies SMS messages as **Spam** or **Ham (Not Spam)**.

---

## Objectives

- Convert text into numerical vectors
- Train a classification model
- Evaluate model accuracy
- Predict custom messages

---

## Workflow

SMS Dataset

↓

Text Cleaning

↓

CountVectorizer

↓

Train/Test Split

↓

Multinomial Naive Bayes

↓

Prediction

---

## Machine Learning Algorithm

**Multinomial Naive Bayes**

Why?

- Fast
- Memory efficient
- Excellent for text classification
- Commonly used in spam filtering

---

## Text Vectorization

Used **CountVectorizer** to convert words into numerical feature vectors that machine learning models can understand.

---

## Model Evaluation

Metrics:

- Accuracy
- Precision
- Recall
- F1 Score

---

## Sample Predictions

| Message | Prediction |
|----------|------------|
| Win a free iPhone now! | Spam |
| Let's meet tomorrow | Ham |
| Claim your cash reward | Spam |
| Good morning! | Ham |

---

## Technologies Used

- Python
- Pandas
- NLTK
- Scikit-learn

---

## Real-World Applications

- Email spam filtering
- SMS fraud detection
- Social media moderation
- Customer support automation
- Content classification

---

## Conclusion

By combining text preprocessing, vectorization, and a Naive Bayes classifier, we built a simple yet effective spam detection system capable of classifying new SMS messages automatically.