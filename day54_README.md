# Day 54 - Smart Spam Detector (Part 1)

## Problem Statement

A messaging company wants to build an AI-powered spam detection system.

The first step is to prepare the dataset by cleaning and preprocessing text before training any machine learning model.

---

## Objectives

* Load the SMS Spam dataset
* Clean and preprocess text
* Remove punctuation
* Remove stopwords
* Explore spam vs ham distribution

---

## Dataset

SMS Spam Collection Dataset

Features:

* label (spam/ham)
* message (SMS text)

---

## Preprocessing Steps

1. Convert text to lowercase
2. Remove punctuation
3. Remove English stopwords
4. Store cleaned text

---

## Data Observations

* Total Messages: 5,572
* Ham Messages: 4,825
* Spam Messages: 747

The dataset is imbalanced, with significantly more legitimate messages than spam.

---

## Why Preprocessing?

Raw text contains unnecessary words and symbols that increase noise.

Cleaning the text improves the quality of features used by machine learning algorithms.

---

## Technologies Used

* Python
* Pandas
* NLTK

---

## Real-World Applications

* Email spam filtering
* SMS fraud detection
* Social media moderation
* Cybersecurity systems

---

## Conclusion

Data preprocessing is a crucial first step in Natural Language Processing (NLP). Well-prepared data leads to better-performing machine learning models.
