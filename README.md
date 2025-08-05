# 📧 Email & SMS Spam Classifier

An interactive web application built with Python and Streamlit that classifies messages as Spam or Ham (Not Spam) using a trained machine learning model. This project showcases the full ML lifecycle—from data preprocessing and model training to deployment as a user-friendly web interface.

🔗 **Live Demo**: [Click here to try the app](https://karantulsani-spam-classifier-app-app-kym0ka.streamlit.app/)

## ✨ Features

- **Naive Bayes Classifier**  
  Uses the Multinomial Naive Bayes algorithm, known for its effectiveness in text classification tasks.

- **TF-IDF Vectorization**  
  Converts text messages into numerical form using Term Frequency–Inverse Document Frequency to enhance model performance.

- **Text Preprocessing**  
  Cleans input data with steps like lowercasing and punctuation removal for better model accuracy.

- **Interactive Web Interface**  
  Built with Streamlit, allowing users to enter a message and receive instant classification results.

## 🧪 Try These Example Messages

### Spam Examples
Paste these into the app to test how it detects spam:

**Prize/Lottery Scam:**  
`Congratulations! You've won a free iPhone 15. To claim your prize, click this link immediately.`

**Investment Scam:**  
`Exclusive Investment Opportunity! Unlock the secret to financial freedom. Our system guarantees a 300% return in just 30 days. Act now!`

**Phishing Alert:**  
`URGENT: Your bank account has been compromised. Click here to verify your identity immediately.`

**Fake Job Offer:**  
`Work From Home - Earn $5000/month. No experience needed. Send your details now to apply.`

### Ham Examples
These should be classified as safe (ham):

**Work Email:**  
`Hi team, just wanted to follow up on the action items from yesterday's meeting. Please update by EOD.`

**Personal Plans:**  
`Hey, are we still on for the meeting tomorrow at 10 AM? Let me know.`

**Order Confirmation:**  
`Thank you for your purchase. Your order #123-4567890 is being processed.`

**Simple Query:**  
`Hi Sarah, I had a quick question about the Q2 financial report. Do you have a moment to chat?`

## 🛠️ Tech Stack

- Python  
- scikit-learn  
- pandas  
- Streamlit  
- Multinomial Naive Bayes  
- TF-IDF Vectorizer  
- Streamlit Cloud for deployment  
