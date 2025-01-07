import streamlit as st
from styles import apply_styles
def show():
    apply_styles()
    # Custom Background Theme using HTML & CSS
    st.markdown("""
        <style>
        body {
            background: linear-gradient(to right, #1e3c72, #2a5298);
            color: white;
            font-family: 'Arial', sans-serif;
        }
        .stTitle {
            color: #FFD700;
            text-align: center;
            font-weight: bold;
            font-size: 40px;
        }
        .stMarkdown {
            color: #FFFFFF;
            font-size: 18px;
        }
        .stButton > button {
            background-color: #FF5733;
            color: white;
            border-radius: 5px;
            padding: 8px 16px;
            font-weight: bold;
        }
        .stButton > button:hover {
            background-color: #C70039;
        }
        hr {
            border: none;
            height: 3px;
            background-color: #FFD700;
            margin: 20px 0;
        }
        </style>
    """, unsafe_allow_html=True)

    # Hero Section with Tagline
    st.title("🏠 Welcome to AI Loan Default Risk Predictor")
    st.markdown("""
    ### 💡 Empowering Financial Decisions with AI  
    Predict loan default risk with the power of **Machine Learning** and **Generative AI**.
    """, unsafe_allow_html=True)
    
    # Decorative Divider
    st.markdown("---")

    # Features Section with Icons
    st.markdown("""
    #### 📌 Features of the App:
    - 🏦 **Loan Default Risk Prediction (Core ML)**:  
      Traditional form-based loan risk prediction using machine learning.
    - 🤖 **Loan Default Risk Prediction (GenAI Chatbot)**:  
      Chatbot-assisted loan risk prediction with conversational AI.
    - 🧑‍💻 **About Me**:  
      Learn more about the developer behind this project.  
    """, unsafe_allow_html=True)

    # Add a colorful divider
    st.markdown("""
    <hr>
    """, unsafe_allow_html=True)

    # Background Image with Styling
    st.markdown("""
        <style>
        .stImage {
            margin-top: 20px;
            border-radius: 15px;
            box-shadow: 0 8px 15px rgba(0, 0, 0, 0.3);
        }
        </style>
    """, unsafe_allow_html=True)

    

    # Call to Action Buttons
    st.markdown("""
    ---
    ### 🚀 Get Started  
    **Choose an option from the sidebar to begin your journey:**  
    """)

    st.image(
        "Images/Homepage.jpg", 
        use_container_width=True, 
        caption="Simplify financial decisions with AI.",
        output_format="JPEG"
    )
