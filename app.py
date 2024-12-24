import streamlit as st
import pickle
import pandas as pd

# Load the trained pipeline model
model = pickle.load(open('Model_pipeline.pkl', 'rb'))

# Page configuration
st.set_page_config(page_title="Loan Prediction App", layout="wide")

# Add a title and description
st.title('🏦 Loan Prediction App')
st.write(
    """
    This app predicts whether a loan will be **approved** or **denied** based on the applicant's information.
    Please fill in the details below to get the prediction.
    """
)

# Input fields in a 2-column layout for better organization
col1, col2 = st.columns(2)

with col1:
    person_income = st.number_input("Income of Applicant ($)", min_value=0, value=50000, step=1000)
    loan_amnt = st.number_input("Loan Amount ($)", min_value=0, value=10000, step=500)
    loan_int_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
    person_emp_length = st.number_input("Employment Length (years)", min_value=0, max_value=50, value=5)

with col2:
    person_age = st.number_input("Age of Applicant", min_value=18, max_value=100, value=30)
    home_ownership = st.selectbox('Home Ownership', ['RENT', 'MORTGAGE', 'OWN', 'OTHER'])
    cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0, value=10, max_value=60)
    loan_intent = st.selectbox(
        "Loan Purpose",
        ["MEDICAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "VENTURE", "PERSONAL", "EDUCATION"]
    )

loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
cb_person_default_on_file = st.sidebar.selectbox("Default on File", ["N", "Y"], help="Has the applicant defaulted before?")

# Prepare input data for prediction
user_input = pd.DataFrame({
    'person_age': [person_age],
    'person_income': [person_income],
    'person_home_ownership': [home_ownership],
    'person_emp_length': [person_emp_length],
    'loan_intent': [loan_intent],
    'loan_grade': [loan_grade],
    'loan_amnt': [loan_amnt],
    'loan_int_rate': [loan_int_rate],
    'cb_person_default_on_file': [cb_person_default_on_file],
    'cb_person_cred_hist_length': [cb_person_cred_hist_length],
})

# Prediction
if st.button("Predict"):
    prediction = model.predict(user_input)
    prediction_text = '"🎉 The loan is likely to be approved!"' if prediction[0] == 1 else '❌ The loan is likely to be denied!'
    st.subheader(f'Prediction: {prediction_text}')

# Sidebar info
st.sidebar.header("About the App")
st.sidebar.write(
    """
    This app uses machine learning to predict loan approvals based on input features.
    Developed with ❤️ using **Streamlit**.
    """
)
