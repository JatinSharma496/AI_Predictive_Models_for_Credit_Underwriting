from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open('Model_pipeline.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():

    data = request.json
    try:
        
        input_data = pd.DataFrame([data])
        
        prediction = model.predict(input_data)

        return jsonify({'prediction': int(prediction[0])})
        
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
