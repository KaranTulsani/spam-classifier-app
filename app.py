import streamlit as st
import joblib
import string

# --- 1. Load the saved Vectorizer and Model ---
# We are loading the files we saved in the training script
try:
    vectorizer = joblib.load('vectorizer.joblib')
    model = joblib.load('model.joblib')
except FileNotFoundError:
    st.error("Model files not found. Please run the 'train_model.py' script first.")
    st.stop() # Stop the app if models aren't found

# --- 2. Create the Preprocessing Function ---
# This function MUST be identical to the one in your training script
def preprocess_text(text):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    return text

# --- 3. Set up the Streamlit App Interface ---
st.set_page_config(page_title="Spam Classifier", page_icon="📧")

st.title("📧 Email & SMS Spam Classifier")
st.write(
    "This app uses a Machine Learning model to classify messages as Spam or Ham (Not Spam). "
    "Enter a message in the text box below and click 'Classify' to see the prediction."
)

# Create a text area for user input
input_message = st.text_area("Enter the message:", height=150)

# Create a button that triggers the prediction
if st.button('Classify', type="primary"):
    if not input_message.strip():
        # Show a warning if the text area is empty
        st.warning("Please enter a message to classify.")
    else:
        # --- 4. Make a Prediction ---
        # Preprocess the user's input message
        processed_message = preprocess_text(input_message)
        
        # Transform the preprocessed message using the loaded vectorizer
        message_vector = vectorizer.transform([processed_message])
        
        # Predict using the loaded Naive Bayes model
        prediction = model.predict(message_vector)[0]
        
        # --- 5. Display the Result ---
        st.subheader("Result:")
        if prediction == 'spam':
            st.error("This message is classified as SPAM.", icon="🚨")
        else:
            st.success("This message is classified as HAM (Not Spam).", icon="✅")

# Add a footer with some information
st.markdown("---")
st.write("Powered by a Multinomial Naive Bayes model and built with Streamlit.")
