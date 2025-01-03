import streamlit as st

import home, loan_core_ml, loan_chatbot, about_me



# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Go to",
    ["Home",  "Loan Prediction (GenAI Chatbot)","Loan Prediction (Core ML)", "About Me"]
)

# Route to pages based on sidebar selection
if app_mode == "Home":
    home.show()
elif app_mode == "Loan Prediction (Core ML)":
    loan_core_ml.show()
elif app_mode == "Loan Prediction (GenAI Chatbot)":
    loan_chatbot.show()
elif app_mode == "About Me":
    about_me.show()
