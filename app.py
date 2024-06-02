from flask import Flask, render_template, request
import joblib
import os
import  numpy as np
import pickle
app= Flask(__name__, static_url_path='/static')
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/analysis")
def analysis():
    return render_template("home.html")
@app.route("/about")
def about():
    return render_template("about.html")
@app.route("/contact")
def contact():
    return render_template("contact.html")
@app.route("/home")
def home():
    return render_template("index.html")
@app.route("/consult")
def consult():
    return render_template("consult.html")

@app.route("/result",methods=['POST','GET'])
def result():
    gender=int(request.form['gender'])
    age=int(request.form['age'])
    hypertension=int(request.form['hypertension'])
    heart_disease = int(request.form['heart_disease'])
    ever_married = int(request.form['ever_married'])
    work_type = int(request.form['work_type'])
    Residence_type = int(request.form['Residence_type'])
    avg_glucose_level = float(request.form['avg_glucose_level'])
    bmi = float(request.form['bmi'])
    smoking_status = int(request.form['smoking_status'])

    x=np.array([gender,age,hypertension,heart_disease,ever_married,work_type,Residence_type,
                avg_glucose_level,bmi,smoking_status]).reshape(1,-1)

    scaler_path=os.path.join('D:/Stroke-Risk-Prediction-using-Machine-Learning-master','models/scaler.pkl')
    scaler=None
    with open(scaler_path,'rb') as scaler_file:
        scaler=pickle.load(scaler_file)

    x=scaler.transform(x)

    model_path=os.path.join('D:/Stroke-Risk-Prediction-using-Machine-Learning-master','models/dt.sav')
    dt=joblib.load(model_path)

    Y_pred=dt.predict(x)
    probability_of_stroke = (dt.predict_proba(x)[0][1])*100

    # for No Stroke Risk
    if Y_pred==0:
        return render_template('nostroke.html')
    else:
        return render_template('stroke.html',probability=probability_of_stroke)

if __name__=="__main__":
    app.run(debug=True,port=7384)
