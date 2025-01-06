import streamlit as st
import pandas as pd
import pickle
import json
from groq import Groq
import os
from styles import apply_styles
# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
MODEL = 'llama3-groq-70b-8192-tool-use-preview'


@st.cache_resource
def load_model():
    try:
        model_path = 'Application/Model_pipeline.pkl'
        return pickle.load(open(model_path, 'rb'))
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'Model_pipeline.pkl' is in the correct directory.")
        return None
model=load_model()
def get_initial_messages():
    return [
        {
            "role": "system",
            "content": (
                """You are a professional advisor working with banks to assess the likelihood of a borrower defaulting on a loan. 
                Collect user details step by step, focusing on evaluating risk factors such as income, loan amount, credit history, etc. 
                Provide a clear and concise risk report, helping the bank make an informed lending decision."""
            )
        },
        {
            "role": "assistant",
            "content": "Welcome to the Loan Risk Assessment System. Let's analyze the risk profile of the potential borrower. Can you start by providing the applicant's age?"
        }
    ]


def get_loan_default_risk(**kwargs):
    try:
        if model is None:
            return {"error": "Model not loaded. Please try again."}

        user_input = pd.DataFrame([kwargs])
        prediction = model.predict(user_input)[0]
    

        return {
            "default_risk": bool(prediction),
            "input_data": kwargs,
            "message": "High Default Risk" if prediction else "Low Default Risk"
        }
    except Exception as e:
        return {"error": f"Error in prediction: {str(e)}"}

def reset_conversation_state():
    # Clear specific session state variables
    if 'messages' in st.session_state:
        del st.session_state.messages
    if 'collected_data' in st.session_state:
        del st.session_state.collected_data
    if 'current_step' in st.session_state:
        del st.session_state.current_step
    if 'prediction_done' in st.session_state:
        del st.session_state.prediction_done
    
    # Clear any chat-related state
    for key in list(st.session_state.keys()):
        if key.startswith('chat_'):
            del st.session_state[key]
    
    # Initialize new conversation
    st.session_state.messages = get_initial_messages()
    st.session_state.collected_data = {}
    st.session_state.current_step = "start"
    st.session_state.prediction_done = False



def show():
    apply_styles()

    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.title("🏦 Bank Loan Default Risk Assessment")
    st.markdown(
        """
        Chat with our AI-powered advisor to evaluate whether a borrower is likely to default on their loan.
        Provide step-by-step details for a comprehensive analysis.
        """
    )
    st.markdown('</div>', unsafe_allow_html=True)

    if "messages" not in st.session_state:
        st.session_state.messages = get_initial_messages()
        st.session_state.collected_data = {}
        st.session_state.current_step = "start"
        st.session_state.prediction_done = False

    with st.sidebar:
        if st.button("Start New Assessment"):
            reset_conversation_state()
            st.rerun()

    for message in st.session_state.messages:
        if message["role"] != "system":
            with st.chat_message(message["role"]):
                st.markdown(f'<div class="chat-message">{message["content"]}</div>', unsafe_allow_html=True)

    if prompt := st.chat_input("Type your response here..."):
        st.session_state.messages.append({"role": "user", "content": prompt.upper()})
        with st.chat_message("user"):
            st.markdown(f'<div class="chat-message">{prompt.upper()}</div>', unsafe_allow_html=True)

        tools = [{
            "type": "function",
            "function": {
                "name": "loan_default_risk",
                "description": "Predict loan default risk using the trained model",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "person_age": {"type": "integer", "minimum": 18, "maximum": 100},
                        "person_income": {"type": "integer", "minimum": 0},
                        "person_home_ownership": {"type": "string", "enum": ["RENT", "MORTGAGE", "OWN", "OTHER"]},
                        "person_emp_length": {"type": "integer", "minimum": 0, "maximum": 50},
                        "loan_intent": {"type": "string", "enum": ["MEDICAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "VENTURE", "PERSONAL", "EDUCATION"]},
                        "loan_grade": {"type": "string", "enum": ["A", "B", "C", "D", "E", "F", "G"]},
                        "loan_amnt": {"type": "integer", "minimum": 0},
                        "loan_int_rate": {"type": "number", "minimum": 0, "maximum": 100},
                        "cb_person_default_on_file": {"type": "string", "enum": ["N", "Y"]},
                        "cb_person_cred_hist_length": {"type": "integer", "minimum": 0, "maximum": 60}
                    },
                    "required": ["person_age", "person_income", "person_home_ownership", 
                               "person_emp_length", "loan_intent", "loan_grade", "loan_amnt",
                               "loan_int_rate", "cb_person_default_on_file", "cb_person_cred_hist_length"]
                }
            }
        }]

        try:
            with st.chat_message("assistant"):
                with st.spinner("Analyzing borrower details..."):
                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                        tools=tools,
                        tool_choice="auto",
                        max_tokens=4096,
                    )

                    assistant_message = response.choices[0].message.content or "Analyzing borrower details..."
                    st.markdown(f'<div class="chat-message">{assistant_message}</div>', unsafe_allow_html=True)
                    st.session_state.messages.append({
                        "role": "assistant",
                        "content": assistant_message
                    })

                    if response.choices[0].message.tool_calls:
                        tool_call = response.choices[0].message.tool_calls[0]
                        if tool_call.function.name == "loan_default_risk":
                            arguments = json.loads(tool_call.function.arguments)
                            
                            if all(value is not None for value in arguments.values()):
                                risk_result = get_loan_default_risk(**arguments)
                                if "error" not in risk_result:
                                    result_class = "risk-low" if not risk_result["default_risk"] else "risk-high"
                                    result_message = f"""
                                
                                    <div class="{result_class}">
                                    📊 <strong>Risk Assessment Results</strong><br>
                                    {"⚠️ High Default Risk" if risk_result["default_risk"] else "✅ Low Default Risk"}<br><br>
                                    
                                    <strong>Detailed Analysis:</strong><br>
                                    - Age: {arguments['person_age']} years<br>
                                    - Annual Income: ${arguments['person_income']:,}<br>
                                    - Home Ownership: {arguments['person_home_ownership']}<br>
                                    - Employment Length: {arguments['person_emp_length']} years<br>
                                    - Loan Amount: ${arguments['loan_amnt']:,}<br>
                                    - Interest Rate: {arguments['loan_int_rate']}%<br>
                                    - Loan Purpose: {arguments['loan_intent']}<br>
                                    - Loan Grade: {arguments['loan_grade']}<br>
                                    - Credit History Length: {arguments['cb_person_cred_hist_length']} years<br>
                                    - Previous Defaults: {"Yes" if arguments['cb_person_default_on_file'] == "Y" else "No"}<br>
                                    </div>
                                    """
                                    st.markdown(result_message, unsafe_allow_html=True)
                                    st.session_state.messages.append({
                                        "role": "assistant",
                                        "content": result_message
                                    })
                                    st.session_state.prediction_done = True
                                else:
                                    st.error(risk_result["error"])

        except Exception as e:
            error_message = f"I apologize, but I encountered an error: {str(e)}"
            st.error(error_message)
            st.session_state.messages.append({
                "role": "assistant",
                "content": error_message
            })

