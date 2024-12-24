

---

# **AI Predictive models for Credit Underwriting**

A machine learning-based solution to predict loan approvals based on applicant details, financial history, and loan attributes. This project includes feature importance analysis, model training, and a user-friendly web application for real-time predictions.

---

## **Table of Contents**
1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Dataset](#dataset)  
5. [Model and Approach](#model-and-approach)  
6. [Web Application](#web-application)  
7. [Installation](#installation)  
8. [Usage](#usage)  
9. [Results](#results)  
10. [Future Enhancements](#future-enhancements)  
11. [Contributing](#contributing)  
12. [License](#license)  

---

## **Introduction**  
Loan approval decisions are critical for financial institutions. This project leverages machine learning to automate loan eligibility assessments based on historical data. The system provides quick and accurate predictions, aiding lenders in minimizing risks and improving efficiency.

---

## **Features**
- Predicts loan approval using a Gradient Boosting model.
- Provides real-time predictions via a Streamlit web app.
- Displays feature importance for transparency.
- Robust handling of missing or invalid inputs.

---

## **Technologies Used**
- **Programming Language**: Python  
- **Libraries**:
  - Machine Learning: `scikit-learn`, `numpy`, `pandas`
  - Visualization: `matplotlib`, `seaborn`
  - Web App: `streamlit`
- Deployment-ready for local and cloud hosting.

---

## **Dataset**
- **Source**: to be filles  
- **Attributes**:
  - Demographic: `person_age`, `person_income`, `person_emp_length`
  - Loan details: `loan_amnt`, `loan_int_rate`, `loan_intent`, `loan_grade`
  - Credit history: `cb_person_cred_hist_length`, `cb_person_default_on_file`
  - Categorical attributes are one-hot encoded for machine learning compatibility.

---

## **Model and Approach**
1. **Data Preprocessing**:
   - Handled missing values and encoded categorical features.
   - Scaled numerical features for consistent model input.

2. **Model**:
   - to be filled in future 
   - **Gradient Boosting** chosen for its accuracy and interpretability.
   - Features like `person_income` and `loan_amnt` were identified as most important.

4. **Evaluation**:
   - Metrics: Accuracy, Precision, Recall, F1-Score.
   - to bve filled

5. **Deployment**:
   - Streamlit-based app for user-friendly predictions.

---

## **Web Application**
The web application allows users to input loan details and view predictions.  

### **Key Features**:
- Intuitive form-based input for loan attributes.
- Instant predictions with explanations.
- Caches model resources for efficiency.  

### **Screenshots**:  
_TO be uploaded later_

---

## **Installation**
Follow these steps to run the project locally:  

to be filled later

