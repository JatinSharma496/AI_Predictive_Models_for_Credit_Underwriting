import streamlit as st
import pandas as pd
import pickle

# Load model
@st.cache_resource
def load_model():
    try:
        return pickle.load(open('Model_pipeline.pkl', 'rb'))
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'Model_pipeline.pkl' is in the correct directory.")
        return None

model = load_model()

def show():
    st.title("📊 Loan Prediction (Core ML)")
    
    if not model:
        st.error("Model not loaded. Please check the model file.")
    else:
        st.markdown("Fill in the following details to predict loan approval:")

        # Input fields
        person_income = st.number_input("Income of Applicant ($)", min_value=0, value=50000, step=1000)
        loan_amnt = st.number_input("Loan Amount ($)", min_value=0, value=10000, step=500)
        loan_int_rate = st.slider("Interest Rate (%)", min_value=0.0, max_value=100.0, value=5.0, step=0.1)
        person_emp_length = st.number_input("Employment Length (years)", min_value=0, max_value=50, value=5)
        person_age = st.number_input("Age of Applicant", min_value=18, max_value=100, value=30)
        home_ownership = st.selectbox("Home Ownership", ["RENT", "MORTGAGE", "OWN", "OTHER"])
        loan_intent = st.selectbox("Loan Purpose", ["MEDICAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "VENTURE", "PERSONAL", "EDUCATION"])
        loan_grade = st.selectbox("Loan Grade", ["A", "B", "C", "D", "E", "F", "G"])
        cb_person_default_on_file = st.selectbox("Default on File", ["N", "Y"])
        cb_person_cred_hist_length = st.number_input("Credit History Length (years)", min_value=0, value=10, max_value=60)

        # Prediction
        if st.button("Predict"):
            try:
                user_input = pd.DataFrame([{
                    'person_age': person_age,
                    'person_income': person_income,
                    'person_home_ownership': home_ownership,
                    'person_emp_length': person_emp_length,
                    'loan_intent': loan_intent,
                    'loan_grade': loan_grade,
                    'loan_amnt': loan_amnt,
                    'loan_int_rate': loan_int_rate,
                    'cb_person_default_on_file': cb_person_default_on_file,
                    'cb_person_cred_hist_length': cb_person_cred_hist_length,
                }])
                prediction = model.predict(user_input)[0]
                if prediction == 1:
                    # Approved - Green Background
                    st.markdown(
                        '<p style="background-color:green;color:white;padding:10px;border-radius:5px;">🎉 Loan Approved!</p>',
                        unsafe_allow_html=True
                    )
                else:
                    # Not Approved - Red Background
                    st.markdown(
                        '<p style="background-color:red;color:white;padding:10px;border-radius:5px;">❌ Loan Denied!</p>',
                        unsafe_allow_html=True
                    )
            except Exception as e:
                st.error(f"Error during prediction: {e}")
if __name__ == "__main__":
    show()