import pandas as pd
import string
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
import joblib

print("Starting the training process...")

# --- 1. Load Data ---
try:
    # We are now assuming the columns are already named 'Category' and 'Message'
    df = pd.read_csv('email.csv', encoding='latin-1')
except FileNotFoundError:
    print("Error: 'spam.csv' not found. Make sure it's in the same folder as the script.")
    exit()

# --- THIS IS THE FIX ---
# The following two lines have been removed, as your columns are already correct.
# df = df[['v1', 'v2']]
# df.columns = ['Category', 'Message']

# Let's check for and drop any other potential unnecessary columns to be safe
# This makes the code more robust
if 'Unnamed: 2' in df.columns:
    df = df[['Category', 'Message']]


print("Data loaded successfully.")
print("Columns found:", df.columns.tolist())


# --- 2. Preprocess Data ---
def preprocess_text(text):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

df['Message'] = df['Message'].apply(preprocess_text)
print("Text preprocessing complete.")

# --- 3. Split Data ---
X = df['Message']
y = df['Category']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Data split into training and testing sets.")

# --- 4. Feature Extraction (TF-IDF) ---
tfidf_vectorizer = TfidfVectorizer()
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
print("TF-IDF Vectorizer has been fitted.")

# --- 5. Train the Naive Bayes Model ---
naive_bayes_model = MultinomialNB()
naive_bayes_model.fit(X_train_tfidf, y_train)
print("Naive Bayes model has been trained.")

# --- 6. Save the Vectorizer and Model ---
joblib.dump(tfidf_vectorizer, 'vectorizer.joblib')
joblib.dump(naive_bayes_model, 'model.joblib')

print("\nTraining complete!")
print("Model and vectorizer have been saved as 'model.joblib' and 'vectorizer.joblib'")
