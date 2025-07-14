from flask import Flask, request, jsonify #request is the property of flask
import pandas as pd
import pickle

app = Flask(__name__)

# Define the endpoint
@app.route("/predict", methods=['POST'])
def get_prediction():
    #Get data from the user
    baby_data = request.get_json()

    #convert into dataframe
    baby_df =  pd.DataFrame(baby_data)

    #Load the trained machine learning model 
    with open("model/model.pkl",'rb') as obj:
        model = pickle.load(obj)

    #Make prediction on user data
    prediction = model.predict(baby_df)
    prediction = round(float(prediction),2)

    #Return response in json format
    response = {"Prediction ":prediction}

    return jsonify(response)

if __name__=='__main__':
    app.run(debug=True)