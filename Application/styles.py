import streamlit as st

def apply_styles():
    st.markdown("""
        <style>
        .stApp {
            background-color: #0A192F;
            color: #E2E8F0;
        }

        .chat-container {
            background: linear-gradient(145deg, #1A365D, #2D3748);
            padding: 2rem;
            border-radius: 15px;
            margin-bottom: 1rem;
        }

        .chat-message {
            background-color: #1E293B;
            padding: 1rem;
            border-radius: 10px;
            margin: 0.5rem 0;
        }

        .risk-low {
            background: linear-gradient(145deg, #059669, #047857);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }

        .risk-high {
            background: linear-gradient(145deg, #DC2626, #B91C1C);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            margin: 1rem 0;
        }

        .stButton > button {
            background: linear-gradient(90deg, #3B82F6, #2563EB);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
        }

        .stButton > button:hover {
            background: linear-gradient(90deg, #2563EB, #1D4ED8);
            transform: translateY(-2px);
        }

        .stTextInput > div > div > input {
            background-color: #1E293B;
            color: #E2E8F0;
            border: 1px solid #4A5568;
            border-radius: 8px;
        }

        
        </style>

    """, unsafe_allow_html=True)

def core_ml_apply_styles():
    st.markdown("""
        <style>
        /* Main theme and container styles */
        .stApp {
            background-color: #0A192F;
            color: #E2E8F0;
        }
        
        .main-container {
            background: linear-gradient(145deg, #1A365D, #2D3748);
            padding: 2rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            margin-bottom: 2rem;
        }
        
        /* Risk assessment indicators */
        .risk-low {
            background: linear-gradient(145deg, #059669, #047857);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(5, 150, 105, 0.2);
            text-align: center;
            font-size: 1.2rem;
            margin: 1rem 0;
        }
        
        .risk-high {
            background: linear-gradient(145deg, #DC2626, #B91C1C);
            color: white;
            padding: 1.5rem;
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(220, 38, 38, 0.2);
            text-align: center;
            font-size: 1.2rem;
            margin: 1rem 0;
        }
        
        /* Input field styling */
        .stNumberInput, .stSlider, .stSelectbox {
            background-color: #1E293B;
            border-radius: 6px;
            padding: 0.5rem;
            margin: 0.5rem 0;
        }
        .stSlider {
            background-color: #1E293B;
            border-radius: 6px;
            padding: 0rem;
            margin: 0.5rem 0;
        }
        
        /* Button styling */
        .stButton > button {
            background: linear-gradient(90deg, #3B82F6, #2563EB);
            color: white;
            border: none;
            padding: 0.75rem 1.5rem;
            border-radius: 8px;
            font-weight: bold;
            transition: all 0.3s ease;
            width: 100%;
        }
        
        .stButton > button:hover {
            background: linear-gradient(90deg, #2563EB, #1D4ED8);
            transform: translateY(-2px);
        }
        
        /* Section headers */
        .section-header {
            background: linear-gradient(90deg, #4B5563, #1F2937);
            padding: 1rem;
            border-radius: 8px;
            margin: 1.5rem 0;
            font-weight: bold;
        }
        
        /* Tooltip styling */
        .tooltip {
            position: relative;
            display: inline-block;
            border-bottom: 1px dotted #CBD5E0;
            cursor: help;
        }
        
        .tooltip .tooltiptext {
            visibility: hidden;
            background-color: #2D3748;
            color: #E2E8F0;
            text-align: center;
            padding: 5px;
            border-radius: 6px;
            position: absolute;
            z-index: 1;
            bottom: 125%;
            left: 50%;
            margin-left: -60px;
            opacity: 0;
            transition: opacity 0.3s;
        }
        
        .tooltip:hover .tooltiptext {
            visibility: visible;
            opacity: 1;
        }
        </style>
    """, unsafe_allow_html=True)
