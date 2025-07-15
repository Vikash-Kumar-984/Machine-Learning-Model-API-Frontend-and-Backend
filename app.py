from flask import Flask, request, jsonify ,render_template #request is the property of flask
import pandas as pd
import pickle

app = Flask(__name__)

# Define the endpoint

def get_cleaned_data():
    gestation =  form_data['gestation']
    parity =  form_data['parity']
    age =  form_data['age']
    height =  form_data['height']
    weight =  form_data['weight']
    smoke =  form_data['smoke']
    
    return cleaned_data

@app.route('/',methods=['GET'])
def home():
    return render_template("index.html")

@app.route("/predict", methods=['POST'])
def get_prediction():
    #Get data from the user
    # baby_data = request.get_json()
    baby_data_form= request.form

    baby_data_cleaned = get_cleaned_data(baby_data_form)


    #convert into dataframe
    baby_df =  pd.DataFrame(baby_data_cleaned)

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