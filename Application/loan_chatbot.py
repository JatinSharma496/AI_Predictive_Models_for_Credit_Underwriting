import streamlit as st
import pickle
import json
import pandas as pd
from groq import Groq
import os 

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))  
MODEL = 'llama3-groq-70b-8192-tool-use-preview'

@st.cache_resource
def load_model():
    try:
        model_path = 'Application\Model_pipeline.pkl'  # Relative to Application folder
        return pickle.load(open(model_path, 'rb'))
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'Model_pipeline.pkl' is in the correct directory.")
        return None

def get_loan_eligibility(person_age, person_income, person_home_ownership, person_emp_length,
                        loan_intent, loan_grade, loan_amnt, loan_int_rate,
                        cb_person_default_on_file, cb_person_cred_hist_length):
    try:
        model = load_model()
        if model is None:
            return {"error": "Model loading failed"}
        
        user_input = pd.DataFrame([{
            'person_age': person_age,
            'person_income': person_income,
            'person_home_ownership': person_home_ownership,
            'person_emp_length': person_emp_length,
            'loan_intent': loan_intent,
            'loan_grade': loan_grade,
            'loan_amnt': loan_amnt,
            'loan_int_rate': loan_int_rate,
            'cb_person_default_on_file': cb_person_default_on_file,
            'cb_person_cred_hist_length': cb_person_cred_hist_length,
        }])
        
        prediction = model.predict(user_input)[0]
        
        result = {
            "eligibility": bool(prediction),
            "input_data": user_input.to_dict(orient='records')[0],
            "message": "Eligible for loan" if prediction else "Not eligible for loan"
        }
        
        return result
    except Exception as e:
        return {"error": f"Failed to process loan eligibility: {str(e)}"}

def get_initial_messages():
    return [
        {
            "role": "system",
            "content": (
                """You are a loan eligibility assistant. 
                Your role is to provide users with detailed, polite, and clear information about their loan eligibility predictions. 
                Gather the required user details step by step, asking one question at a time,
                and avoid requesting all the information at once.
                Only after collecting all the necessary details, proceed to predict the loan eligibility."""
            )
        },
        {
            "role": "assistant",
            "content": "Hello! I'm your loan eligibility assistant. I can help you check if you're eligible for a loan. Would you like to proceed with the assessment?"
        }
    ]

def reset_conversation_state():
   
    # Clear all conversation-related session state
    st.session_state.messages = get_initial_messages()
    st.session_state.current_step = "start"
    st.session_state.collected_data = {}
    # Clear any other related session state variables you might have
    for key in list(st.session_state.keys()):
        if key.startswith('chat_'):  # Clear any chat-related state
            del st.session_state[key]

def show():
    st.title("🤖 Loan Prediction (GenAI Chatbot)")
    st.markdown("""
    Chat with our AI-powered chatbot to get personalized loan predictions.  
    Simply answer the questions, and the chatbot will guide you.
    """)

    # Initialize session state variables if they don't exist
    if "messages" not in st.session_state:
        st.session_state.messages = get_initial_messages()
        st.session_state.current_step = "start"
        st.session_state.collected_data = {}
        
    # Handle "Start New Conversation" button
    if st.sidebar.button("Start New Conversation", key='reset_button'):
        reset_conversation_state()
        st.rerun()  # Force a complete rerun of the app

    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] != "system":  # Skip system messages
            with st.chat_message(message["role"]):
                st.write(message["content"])

    # User input handling
    prompt = st.chat_input("Type your message here...")
    if prompt:
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Define tools for the model
        tools = [{
            "type": "function",
            "function": {
                "name": "loan_eligibility",
                "description": "Predict loan eligibility using the trained model",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "person_age": {
                            "type": "integer",
                            "minimum": 18,
                            "maximum": 100,
                            "description": "Age of the applicant"
                        },
                        "person_income": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Annual income of the applicant in dollars"
                        },
                        "person_home_ownership": {
                            "type": "string",
                            "enum": ["RENT", "MORTGAGE", "OWN", "OTHER"],
                            "description": "Home ownership status"
                        },
                        "person_emp_length": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 50,
                            "description": "Length of employment in years"
                        },
                        "loan_intent": {
                            "type": "string",
                            "enum": ["MEDICAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "VENTURE", "PERSONAL", "EDUCATION"],
                            "description": "Purpose of the loan"
                        },
                        "loan_grade": {
                            "type": "string",
                            "enum": ["A", "B", "C", "D", "E", "F", "G"],
                            "description": "Grade of the loan"
                        },
                        "loan_amnt": {
                            "type": "integer",
                            "minimum": 0,
                            "description": "Requested loan amount in dollars"
                        },
                        "loan_int_rate": {
                            "type": "number",
                            "minimum": 0,
                            "maximum": 100,
                            "description": "Interest rate of the loan as a percentage"
                        },
                        "cb_person_default_on_file": {
                            "type": "string",
                            "enum": ["N", "Y"],
                            "description": "Whether applicant has a default on file"
                        },
                        "cb_person_cred_hist_length": {
                            "type": "integer",
                            "minimum": 0,
                            "maximum": 60,
                            "description": "Length of credit history in years"
                        }
                    },
                    "required": ["person_age", "person_income", "person_home_ownership", 
                               "person_emp_length", "loan_intent", "loan_grade", "loan_amnt",
                               "loan_int_rate", "cb_person_default_on_file", "cb_person_cred_hist_length"]
                }
            }
        }]

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    # Get initial response from the model
                    response = client.chat.completions.create(
                        model=MODEL,
                        messages=[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                        stream=False,
                        tools=tools,
                        tool_choice="auto",
                        max_tokens=4096,
                    )

                    response_message = response.choices[0].message
                    tool_calls = response_message.tool_calls

                    # Handle tool calls (loan eligibility prediction)
                    if tool_calls:
                        for tool_call in tool_calls:
                            if tool_call.function.name == "loan_eligibility":
                                function_args = json.loads(tool_call.function.arguments)
                                
                                # Store the collected data
                                st.session_state.collected_data = function_args
                                
                                # Get prediction
                                function_response = get_loan_eligibility(**function_args)

                                if "error" not in function_response:
                                    result_message = f"""
                                    📊 **Loan Assessment Results**

                                    {'✅ Eligible for Loan' if function_response['eligibility'] else '❌ Not Eligible for Loan'}

                                    ### **Personal Details:**
                                    - Age: {function_args['person_age']} years
                                    - Income: ${function_args['person_income']:,}
                                    - Home Ownership: {function_args['person_home_ownership']}
                                    - Employment Length: {function_args['person_emp_length']} years

                                    ### **Loan Details:**
                                    - Loan Amount: ${function_args['loan_amnt']:,}
                                    - Interest Rate: {function_args['loan_int_rate']}%
                                    - Loan Purpose: {function_args['loan_intent']}
                                    - Loan Grade: {function_args['loan_grade']}

                                    ### **Credit Details:**
                                    - Credit Default on File: {'Yes' if function_args['cb_person_default_on_file'] == 'Y' else 'No'}
                                    - Credit History Length: {function_args['cb_person_cred_hist_length']} years
                                    """
                                else:
                                    result_message = f"⚠️ Error: {function_response['error']}"

                                st.markdown(result_message)
                                st.session_state.messages.append({"role": "assistant", "content": result_message})

                                # Get final response
                                second_response = client.chat.completions.create(
                                    model=MODEL,
                                    messages=[*st.session_state.messages]
                                )
                                final_response = second_response.choices[0].message.content
                                st.write(final_response)
                                st.session_state.messages.append({"role": "assistant", "content": final_response})
                    else:
                        st.write(response_message.content)
                        st.session_state.messages.append({"role": "assistant", "content": response_message.content})

                except Exception as e:
                    error_message = f"Sorry, I encountered an error: {str(e)}"
                    st.error(error_message)
                    st.session_state.messages.append({"role": "assistant", "content": error_message})
