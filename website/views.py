from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import ContactUs
from . import db
import json
import joblib
import pickle
import numpy as np
import os

views = Blueprint('views', __name__)

with open('website\model4.pkl','rb') as f:
    filename = pickle.load(f)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("index.html", user=current_user)

@views.route("/index")
@login_required
def index():
    return render_template("index.html", user=current_user)

@views.route("/about")
@login_required
def about():
    return render_template("about.html", user=current_user)

@views.route("/cancer")
@login_required
def cancer():
    return render_template("cancer.html", user=current_user)

@views.route("/diabetes")
@login_required
def diabetes():
    return render_template("diabetes.html", user=current_user)

@views.route("/heart")
@login_required
def heart():
    return render_template("heart.html", user=current_user)

@views.route("/faq")
@login_required
def faq():
    return render_template("faq.html", user=current_user)

@views.route("/contact", methods=['GET', 'POST'])
@login_required
def contact():
    if request.method == "POST":
        emailid = request.form.get('emailid')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        mobnum = request.form.get('mobnum')
        message = request.form.get('message')
        
        new_message = ContactUs(fname=fname, lname=lname, emailid=emailid, message=message, mobnum=mobnum)
        db.session.add(new_message)
        db.session.commit()
    return render_template("contact.html", user=current_user)


def ValuePredictor(to_predict_list, size):
    to_predict = np.array(to_predict_list).reshape(1,size)
    if(size==8):#Diabetes
        loaded_model = joblib.load("website\model")
        result = loaded_model.predict(to_predict)
    elif(size==30):#Cancer
        loaded_model = joblib.load("website\model1")
        result = loaded_model.predict(to_predict)
    elif(size==11):#Heart
        loaded_model = joblib.load("website\model2")
        result =loaded_model.predict(to_predict)
    return result[0]

@views.route('/result',methods = ["POST"])
@login_required
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
    return(render_template("result.html", prediction=prediction, user=current_user))

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})
