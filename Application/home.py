import streamlit as st
import os

def show():
    st.title("🏠 Welcome to AI Loan Default Risk Predictor")
    
    st.markdown("""
    This app predicts the risk of loan default using Machine Learning and Conversational AI.  
    Select a feature from the sidebar to explore:

    - **Loan Default Risk Prediction (Core ML)**: Traditional form-based loan risk prediction.  
    - **Loan Default Risk Prediction (GenAI Chatbot)**: Chatbot-assisted loan risk prediction using Generative AI.  
    - **About Me**: Learn more about the developer behind this project.  
    """)

    # Adding a background image for style
    st.markdown(
        """
        <style>
        .stImage {
            margin-top: 20px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Display image with enhanced style
    st.image("Images\Homepage.jpg", use_container_width=True, caption="Loan Default Risk Prediction Image", output_format="JPEG")

    # Footer (optional)
    st.markdown("---")

