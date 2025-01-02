import streamlit as st
from pages import home_page, loan_core_ml, loan_chatbot, about_me
import os
import shutil


# Set page config
st.set_page_config(
    page_title="AI Loan Advisor",
    page_icon="💰",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Go to",
    ["Home", "Loan Prediction (Core ML)", "Loan Prediction (GenAI Chatbot)", "About Me"]
)
# Route to pages based on sidebar selection
if app_mode == "Home":
    home_page.show()
elif app_mode == "Loan Prediction (Core ML)":
    loan_core_ml.show()
elif app_mode == "Loan Prediction (GenAI Chatbot)":
    loan_chatbot.show()
elif app_mode == "About Me":
    about_me.show()
