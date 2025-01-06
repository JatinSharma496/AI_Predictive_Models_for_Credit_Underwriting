import streamlit as st
import pandas as pd
import pickle
from styles import core_ml_apply_styles

def load_model():
    try:
        return pickle.load(open('Application/Model_pipeline.pkl', 'rb'))
    except FileNotFoundError:
        st.error("Model file not found. Please ensure 'Model_pipeline.pkl' is in the correct directory.")
        return None


def show():
    core_ml_apply_styles()
    
    st.markdown('<div class="main-container">', unsafe_allow_html=True)
    st.title("🎯 Loan Default Risk Assessment")
    st.markdown("""
    This system analyzes applicant data to predict the likelihood of loan default.
    """)
    st.markdown('</div>', unsafe_allow_html=True)
    
    model = load_model()
    
    if not model:
        st.error("Risk assessment model not loaded. Please check the model file.")
    else:
        st.markdown('<div class="section-header">📋 Applicant Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            person_age = st.number_input(
                "Age", 
                min_value=18, 
                max_value=100, 
                value=30,
                help="Applicant's current age"
            )
            
            home_ownership = st.selectbox(
                "Home Ownership Status", 
                ["RENT", "MORTGAGE", "OWN", "OTHER"],
                help="Current housing situation"
            )
            
            loan_amnt = st.number_input(
                "Requested Loan Amount ($)", 
                min_value=0, 
                value=10000, 
                step=500,
                help="Amount of loan requested"
            )
            loan_intent = st.selectbox(
                "Loan Purpose", 
                ["MEDICAL", "DEBTCONSOLIDATION", "HOMEIMPROVEMENT", "VENTURE", "PERSONAL", "EDUCATION"],
                help="Primary purpose for the loan"
            )
            cb_person_cred_hist_length = st.number_input(
                "Credit History Length (years)", 
                min_value=0, 
                value=10, 
                max_value=60,
                help="Length of credit history in years"
            )
        
        with col2:
            person_income = st.number_input(
                "Annual Income ($)", 
                min_value=0, 
                value=50000, 
                step=1000,
                help="Applicant's annual income before taxes"
            )

            person_emp_length = st.number_input(
                "Employment Length (years)", 
                min_value=0, 
                max_value=50, 
                value=5,
                help="Years at current employment"
            )
            
            loan_int_rate = st.slider(
                "Interest Rate (%)", 
                min_value=0.0, 
                max_value=30.0, 
                value=5.0, 
                step=0.1,
                help="Annual interest rate for the loan"
            )
        
            
            loan_grade = st.selectbox(
                "Loan Grade", 
                ["A", "B", "C", "D", "E", "F", "G"],
                help="Loan grade based on credit assessment"
            )
            

            cb_person_default_on_file = st.selectbox(
                "Previous Defaults", 
                ["N", "Y"],
                help="Whether the applicant has defaulted on previous loans"
            )
        
        if st.button("Analyze Default Risk"):
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
                
                st.markdown('<div class="section-header">📊 Risk Assessment Results</div>', unsafe_allow_html=True)
                
                if prediction == 0:
                    st.markdown(
                        f'''
                        <div class="risk-low">
                            ✅ Low Default Risk
                            <br>
                            <br>
                            <small>The applicant shows good indicators for loan repayment</small>
                        </div>
                        ''',
                        unsafe_allow_html=True
                    )
                else:
                    st.markdown(
                        f'''
                        <div class="risk-high">
                            ⚠️ High Default Risk
                            <br> 
                            <br>
                            <small>The applicant shows elevated risk indicators for default</small>
                        </div>
                        ''',
                        unsafe_allow_html=True
                    )
                
                '''
                st.markdown("### Key Risk Factors")
                col1, col2, col3 = st.columns(3)
                
                with col1:
                    st.metric(
                        "Debt-to-Income Ratio",
                        f"{(loan_amnt / person_income * 100):.1f}%",
                        delta="-Good" if (loan_amnt / person_income) < 0.3 else "+Concern",
                        delta_color="normal"
                    )
                
                with col2:
                    st.metric(
                        "Credit Grade",
                        loan_grade,
                        delta="-Good" if loan_grade in ['A', 'B'] else "+Concern",
                        delta_color="normal"
                    )
                
                with col3:
                    st.metric(
                        "Default History",
                        "Yes" if cb_person_default_on_file == 'Y' else "No",
                        delta="+Concern" if cb_person_default_on_file == 'Y' else "-Good",
                        delta_color="normal"
                    )
                     '''
            except Exception as e:
                st.error(f"Error during risk assessment: {e}")

