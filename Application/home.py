import streamlit as st
import os

st.set_page_config(
    page_title="AI Loan Advisor",
    page_icon="🏦",
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("🏠 Welcome to AI Loan Advisor")
st.markdown("""
This app predicts loan approvals using Machine Learning and Conversational AI.  
Select a feature from the sidebar to explore:

- **Loan Prediction (Core ML)**: Traditional form-based loan prediction.  
- **Loan Prediction (GenAI Chatbot)**: Chatbot-assisted loan prediction using Generative AI.  
- **About Me**: Learn more about the developer behind this project.  
""")

# Placeholder for an image or GIF
st.image("J:\interrnship\Images\loan_image.jpg", use_container_width=True)

