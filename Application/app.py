import streamlit as st

import home, loan_core_ml, loan_chatbot, about_me
#st.set_page_config(page_title="BANK", page_icon="🏦", layout="wide",initial_sidebar_state="collapsed")


# Sidebar Navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio(
    "Go to",
    ["Home",  "Loan Default Prediction (GENAI Chatbot)","Loan Default Prediction", "About Me"],
)

# Route to pages based on sidebar selection
if app_mode == "Home":
    home.show()
elif app_mode == "Loan Default Prediction":
    loan_core_ml.show()
elif app_mode == "Loan Default Prediction (GENAI Chatbot)":
    loan_chatbot.show()
elif app_mode == "About Me":
    about_me.show()
