import streamlit as st
import pandas as pd
import joblib  # Use joblib instead of pickle

# Load pre-trained model
@st.cache_resource
def load_model():
    return joblib.load("GB_model.pkl")  # Load model with joblib

model = load_model()

# Streamlit App
st.title("Loan Approval Prediction")

st.sidebar.header("Input Features")
# Input fields for user
person_age = st.sidebar.number_input("Age of Applicant", min_value=18, max_value=100, value=30)
person_income = st.sidebar.number_input("Income of Applicant ($)", min_value=0, value=50000)
person_emp_length = st.sidebar.number_input("Employment Length (years)", min_value=0, max_value=50, value=5)
loan_amnt = st.sidebar.number_input("Loan Amount ($)", min_value=0, value=10000)
loan_int_rate = st.sidebar.number_input("Interest Rate (%)", min_value=0.0, max_value=100.0, value=5.0)
cb_person_cred_hist_length = st.sidebar.number_input("Credit History Length (years)", min_value=0, value=10)

# Dropdowns for categorical features
person_home_ownership = st.sidebar.selectbox(
    "Home Ownership",
    ["MORTGAGE", "OWN", "RENT", "OTHER"]
)
loan_intent = st.sidebar.selectbox(
    "Loan Purpose",
    ["DEBTCONSOLIDATION", "EDUCATION", "HOMEIMPROVEMENT", "MEDICAL", "PERSONAL", "VENTURE"]
)
loan_grade = st.sidebar.selectbox(
    "Loan Grade",
    ["A", "B", "C", "D", "E", "F", "G"]
)
cb_person_default_on_file = st.sidebar.selectbox(
    "Default on File",
    ["N", "Y"]
)

# Convert inputs into a single row dataframe
def create_input_data():
    # Initialize a dictionary with all features set to 0
    data = {
        'person_age': [0],
        'person_income': [0],
        'person_emp_length': [0],
        'loan_amnt': [0],
        'loan_int_rate': [0],
        'cb_person_cred_hist_length': [0],
        'person_home_ownership_MORTGAGE': [0],
        'person_home_ownership_OTHER': [0],
        'person_home_ownership_OWN': [0],
        'person_home_ownership_RENT': [0],
        'loan_intent_DEBTCONSOLIDATION': [0],
        'loan_intent_EDUCATION': [0],
        'loan_intent_HOMEIMPROVEMENT': [0],
        'loan_intent_MEDICAL': [0],
        'loan_intent_PERSONAL': [0],
        'loan_intent_VENTURE': [0],
        'loan_grade_A': [0],
        'loan_grade_B': [0],
        'loan_grade_C': [0],
        'loan_grade_D': [0],
        'loan_grade_E': [0],
        'loan_grade_F': [0],
        'loan_grade_G': [0],
        'cb_person_default_on_file_N': [0],
        'cb_person_default_on_file_Y': [0],
    }

    # Update the dictionary with user-provided inputs
    data['person_age'] = [person_age]
    data['person_income'] = [person_income]
    data['person_emp_length'] = [person_emp_length]
    data['loan_amnt'] = [loan_amnt]
    data['loan_int_rate'] = [loan_int_rate]
    data['cb_person_cred_hist_length'] = [cb_person_cred_hist_length]
    data[f'person_home_ownership_{person_home_ownership}'] = [1]
    data[f'loan_intent_{loan_intent}'] = [1]
    data[f'loan_grade_{loan_grade}'] = [1]
    data[f'cb_person_default_on_file_{cb_person_default_on_file}'] = [1]

    # Convert to DataFrame with the correct column order
    return pd.DataFrame(data)


input_data = create_input_data()

# Predict button
if st.button("Predict Loan Approval"):
    prediction = model.predict(input_data)[0]  # Assuming binary output: 0 (Not Approved), 1 (Approved)
    if prediction == 1:
        st.success("Congratulations! Your loan is likely to be approved.")
    else:
        st.error("Sorry, your loan is unlikely to be approved.")
