# Day 56 - Smart Spam Detector (Part 3)

## Project Overview

This project deploys the Smart Spam Detector as an interactive web application using **Streamlit**. Users can enter any SMS message and receive an instant prediction indicating whether it is Spam or Ham.

---

## Features

- Interactive web interface
- Real-time spam prediction
- Text preprocessing
- Machine learning model using Multinomial Naive Bayes
- Simple and user-friendly interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NLTK
- Scikit-learn

---

## Project Workflow

SMS Input

↓

Text Cleaning

↓

CountVectorizer

↓

Naive Bayes Model

↓

Spam / Ham Prediction

---

## How to Run

1. Install dependencies:

pip install -r requirements.txt

2. Start the application:

streamlit run app.py

3. Open the browser at:

http://localhost:8501

---

## Sample Messages

Spam:
Congratulations! You won ₹50,000. Click here to claim.

Ham:
Are we meeting after class today?

---

## Real-World Applications

- Email filtering
- SMS fraud detection
- Customer support automation
- Social media moderation
- Content classification

---

## Conclusion

This project demonstrates the complete journey from data preprocessing and machine learning to deploying an interactive AI-powered application.