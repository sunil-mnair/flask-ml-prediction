import os
from flask import Flask,render_template,request, redirect,url_for,Response,jsonify,flash,send_file


from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField

from forms import UploadForm,BuildModelForm
from werkzeug.utils import secure_filename

from flask_bootstrap import Bootstrap

from data_processing import predict_with_ml,buildmodel

app = Flask(__name__)
Bootstrap(app)

app.config['SECRET_KEY'] = 'penroseapp'

@app.route('/')
def index():
    return render_template("index.html")




@app.route('/apply_model',methods=['GET','POST'])
def apply_model():
    form = UploadForm()
    
    if form.validate_on_submit():
       
        new_data = secure_filename(form.new_data.data.filename)
        
        form.new_data.data.save(new_data)

        df = predict_with_ml(new_data)
        
        return render_template('ml_predictions.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

    return render_template('apply_model.html', form = form)

