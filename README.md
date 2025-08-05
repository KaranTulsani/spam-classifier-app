#📧 Email & SMS Spam Classifier
This is a web application built with Python and Streamlit that uses a Machine Learning model to classify messages as either "Spam" or "Ham" (not spam). The project demonstrates a complete ML workflow, from data preprocessing and model training to deployment as an interactive web app.

https://karantulsani-spam-classifier-app-app-kym0ka.streamlit.app/

#✨ Features
Naive Bayes Model: Utilizes a Multinomial Naive Bayes classifier, a fast and effective algorithm for text classification.

TF-IDF Vectorization: Converts text messages into meaningful numerical features using Term Frequency-Inverse Document Frequency.

Basic Text Preprocessing: Includes lowercasing and removal of punctuation for cleaning the text data.

Interactive Web Interface: A user-friendly app built with Streamlit where you can enter any message and get an instant classification.

#🧪 Examples to Test
Here are some examples you can copy and paste into the application to see the model in action.

Spam Examples (Should be classified as SPAM)
Prize / Lottery Scam:

Congratulations! You've won a free iPhone 15. To claim your prize, click this link immediately.

Financial / Investment Scam:

Exclusive Investment Opportunity! Unlock the secret to financial freedom. Our system guarantees a 300% return in just 30 days. Limited spots available. Act now or miss out on a lifetime of wealth.

Urgent / Phishing Alert:

URGENT: Your bank account has been compromised. Please verify your identity immediately by clicking here to secure your funds.

Fake Job Offer:

Work From Home Opportunity - Earn $5000/month. We are looking for data entry clerks. No experience needed. Flexible hours. Reply with your personal details to get started.

Ham Examples (Should be classified as HAM)
Work-related:

Hi team, just wanted to follow up on the action items from yesterday's meeting. Can everyone please provide their updates by EOD?

Personal Plans:

Hey, are we still on for the meeting tomorrow at 10 AM? Let me know. Hope to see you there!

Order Confirmation:

Thank you for your purchase. Your order #123-4567890 is being processed and is expected to ship within 2-3 business days.

Simple Question:

Hi Sarah, I was reviewing the Q2 financial report and had a quick question about the numbers on page 5. Do you have a moment to chat this afternoon?
