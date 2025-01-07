import streamlit as st
import home, loan_core_ml, loan_chatbot, about_me
from styles import app_styles
# Set page config with default collapsed sidebar
st.set_page_config(
    page_title="BANK",
    page_icon="🏦",
    layout="wide",

)
app_styles()

# Sidebar Navigation
st.sidebar.title("Navigation 🧭")
app_mode = st.sidebar.radio(
    "Go to:",
    ["Home", "Prediction (Traditional)", "Chatbot (GEN-AI)", "About Me"],
)

# Route to pages based on sidebar selection
if app_mode == "Home":
    home.show()
elif app_mode == "Prediction (Traditional)":
    loan_core_ml.show()
elif app_mode == "Chatbot (GEN-AI)":
    loan_chatbot.show()
elif app_mode == "About Me":
    about_me.show()
