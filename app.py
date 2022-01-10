from flask import Flask,render_template
import joblib
import pickle
from flask import request
import numpy as np
import os

app=Flask(__name__,template_folder='templates')
flag=1
dir_path = os.path.dirname(os.path.realpath(__file__))
filename = 'model4.pkl'
model4 = pickle.load(open(filename,'rb'))
@app.route("/")

@app.route("/index")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/cancer")
def cancer():
    return render_template("cancer.html")

@app.route("/diabetes")
def diabetes():
    return render_template("diabetes.html")

@app.route("/heart")
def heart():
    return render_template("heart.html")

@app.route("/faq")
def faq():
    return render_template("faq.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/login")
def login():
    return render_template("signin.html")

@app.route("/signup")
def signup():
    return render_template("signup.html")


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = joblib.load("model")
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = joblib.load("model1")
        result = loaded_model.predict(to_predict)
    elif(size==11):#Heart
        loaded_model = joblib.load("model2")
        result =loaded_model.predict(to_predict)
    return result[0]

@app.route('/result',methods = ["POST"])
def result():
    if request.method == 'POST':
        to_predict_list = request.form.to_dict()
        to_predict_list=list(to_predict_list.values())
        to_predict_list = list(map(float, to_predict_list))
        if(len(to_predict_list)==8):#Diabetes
            result = ValuePredictor(to_predict_list,8)
            flag=0
        elif(len(to_predict_list)==30):#Cancer
            result = ValuePredictor(to_predict_list,30)
            flag=0
        elif(len(to_predict_list)==11):#heart
            result = ValuePredictor(to_predict_list,11)
            flag=0

    if(flag==0):
        if(int(result)==1):
            prediction='Looks like you are Suffering!'
        else:
            prediction='You are Healthy for now. Take Care!' 
    return(render_template("result.html", prediction=prediction))

if __name__ == "__main__":
    app.run(debug=True)