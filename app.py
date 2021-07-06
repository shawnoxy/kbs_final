from flask import Flask, render_template, request

import pred

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def hello():
    prediction = '?'
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        cp = request.form['cp']
        trestbps = request.form['trestbps']
        chol = request.form['chol']
        fbs = request.form['fbs']
        restecg = request.form['restecg']
        thalach = request.form['thalach']
        exang = request.form['exang']
        oldpeak = request.form['oldpeak']
        slope = request.form['slope']
        ca = request.form['ca']
        thal = request.form['thal']

        prediction = pred.heart_pred([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])
        prediction = (prediction)[0][0] * 100

    return render_template('index.html', prediction = prediction)
    

@app.route("/sub", methods = ['POST'])
def submit(): 
    if request.method == 'POST':
        name = request.form['username']

    return render_template('sub.html', n = name)
