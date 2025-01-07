

---

# AI Predictive Models for Loan Default Prediction

This project automates the prediction of loan defaults based on applicant details, financial history, and loan attributes using machine learning models. The system includes feature importance analysis, model training, and a user-friendly Flask API and Streamlit web application for real-time predictions. A chatbot has also been integrated for seamless interaction.

## Table of Contents

1. [Introduction](#introduction)  
2. [Features](#features)  
3. [Technologies Used](#technologies-used)  
4. [Dataset](#dataset)  
5. [Model and Approach](#model-and-approach)  
6. [Web Application](#web-application)  
7. [Flask API](#flask-api)  
8. [Chatbot Integration](#chatbot-integration)  
9. [Installation](#installation)  
10. [Usage](#usage)  
11. [Results](#results)  
12. [Future Enhancements](#future-enhancements)  
13. [Learning Resources](#learning-resources)  
14. [License](#license)  

## Introduction

Loan default prediction is a critical task for financial institutions to reduce risks. This project automates the prediction of whether a loan will default based on various applicant details, loan features, and credit history, providing quick and accurate predictions to assist lenders in their decision-making process.

## Features

- **Predictive Modeling**: Uses a Light Gradient Boosting model to predict loan default risk.
- **Real-Time Predictions**: Available through both a Flask API and a Streamlit web app.
- **Feature Importance Analysis**: Highlights the key factors influencing loan default prediction.
- **Robust Input Handling**: Efficient handling of missing or invalid inputs.
- **Chatbot Integration**: A chatbot interface allows users to easily interact with the system for loan default predictions in a conversational manner.

## Technologies Used

- **Programming Language**: Python
- **Libraries**:
  - **Machine Learning**: `scikit-learn`, `numpy`, `pandas`, `lightgbm`
  - **Visualization**: `matplotlib`, `seaborn`
  - **Web Application**: `streamlit`, `flask`
  - **Chatbot**: `streamlit-chatbot`, `GROQ`,`gemma2-9b-it`
- **Deployment**: Docker, Gunicorn, Nginx

## Dataset

- **Source**: [Dataset Source](https://www.kaggle.com/datasets/laotse/credit-risk-dataset)
- **Attributes**:
  - **Demographic**: `person_age`, `person_income`, `person_home_ownership`, `person_emp_length`
  - **Loan Details**: `loan_amnt`, `loan_int_rate`, `loan_intent`, `loan_grade`
  - **Credit History**: `cb_person_cred_hist_length`, `cb_person_default_on_file`
- Categorical features are one-hot encoded, and missing values are imputed during preprocessing.

## Model and Approach

1. **Data Preprocessing**:
   - Handled missing values and one-hot encoded categorical variables.
   - Scaled numerical features for compatibility with machine learning models.

2. **Model**:
   - The model was trained using multiple classification algorithms such as Logistic Regression, Random Forest, AdaBoost, and LightGBM.
   - **Final Model**: Light Gradient Boosting (LightGBM) was selected for its efficiency and high accuracy.

3. **Evaluation**:
   - Metrics: Accuracy, Precision, Recall, F1-Score.
   - LightGBM achieved an accuracy of approximately 93% and an F1-score of around 82%.

4. **Deployment**:
   - The model is deployed with a Flask API and a Streamlit app for real-time interaction.

## Web Application

The Streamlit web application allows users to input loan details and receive a loan default prediction.

### Key Features:
- Simple form-based interface to input loan details.
- Instant loan default predictions with easy-to-understand explanations.

### Live Demo:
[AI Predictive Models for Loan Default Prediction - Streamlit App](https://jatinsharma496-ai-predictive-models-for-loan-default-prediction.streamlit.app/)

## Flask API

The Flask API serves as an interface to interact with the trained loan default prediction model, enabling integration with other systems.

### Key Features:
- POST endpoint to submit loan details and receive a default prediction.
- Handles JSON input and output, ensuring easy integration.
- Robust error handling for invalid input.

### Example Request:

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "person_age": 30,
    "person_income": 50000,
    "person_home_ownership": "MORTGAGE",
    "person_emp_length": 10.0,
    "loan_intent": "PERSONAL",
    "loan_grade": "A",
    "loan_amnt": 20000,
    "loan_int_rate": 6.5,
    "cb_person_default_on_file": "N",
    "cb_person_cred_hist_length": 5
}' http://localhost:5000/predict
```

### Example Response:

```json
{
  "prediction": "No Default"
}
```

## Chatbot Integration

A conversational AI chatbot has been integrated into the system to provide a more interactive and user-friendly experience. The chatbot guides users through the process of entering their loan details and provides predictions in real time.

### Key Features:
- **Interactive**: Users can chat with the system to enter loan details in a conversational manner.
- **Prediction**: The chatbot uses the trained machine learning model to predict whether the loan will default.
- **User-Friendly**: The chatbot interface simplifies the process of loan default prediction for end-users.

### Chatbot Demo:
- The chatbot is available in the [Streamlit App](https://jatinsharma496-ai-predictive-models-for-loan-default-prediction.streamlit.app/), where users can interact with the model in a chat-based format to predict loan defaults.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/JatinSharma496/AI_Predictive_Models_for_Loan_Default_Prediction.git
   cd AI_Predictive_Models_for_Loan_Default_Prediction
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask API**:

   ```bash
   python app.py
   ```

5. **Run the Streamlit App**:

   ```bash
   streamlit run app.py
   ```

## Usage

- **Flask API**: Send POST requests to `http://localhost:5000/predict` with loan details in JSON format or use Postman.
- **Streamlit App**: Navigate to `http://localhost:8501` to input loan details and receive a prediction.
- **Chatbot**: Use the chatbot feature within the Streamlit app to interact with the loan default prediction model.

## Results

The model has been trained and evaluated, achieving high accuracy and providing valuable insights on loan default risk. Key features such as `person_income` and `loan_amnt` have a significant impact on predictions.

![Architecture](Images/Architecture.png)

![Methodology](Images/Methodology.jpeg)

## Future Enhancements

- Incorporate additional data sources to further improve prediction accuracy.
- Add user authentication for a personalized experience.
- Extend chatbot capabilities for deeper conversational insights.

## Learning Resources:

- [YouTube Playlist on Machine Learning](https://youtube.com/playlist?list=PLKnIA16_Rmvbr7zKYQuBfsVkjoLcJgxHH&si=QWJRhsnFwu6etoRT)
- [GeeksforGeeks - LightGBM](https://www.geeksforgeeks.org/lightgbm-light-gradient-boosting-machine/)
- [Kaggle Learn Courses](https://www.kaggle.com/learn)

---

## License:
 - This project is licensed under the MIT License - see the [LICENSE](https://github.com/JatinSharma496/AI_Predictive_Models_for_Loan_Default_Prediction/blob/main/LICENSE) file for details.

Thank you for reading! If you like my project, feel free to give a ⭐ on GitHub!

---
```
