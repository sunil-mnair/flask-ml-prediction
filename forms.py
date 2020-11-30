from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,DateField,SelectField,SubmitField,RadioField
from wtforms.validators import InputRequired,DataRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed
# import phonenumbers

username_required = "Please provide a username"
password_required = "Please provide a password"

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(message=username_required)])
    password = PasswordField('Password',validators=[InputRequired(message=password_required)])
    remember = BooleanField(False)

class SignupForm(FlaskForm):
    username = StringField('Username',validators=[InputRequired(message=username_required)])
    password = PasswordField('Password',validators=[InputRequired(message=password_required)])

class BuildModelForm(FlaskForm):
    xtrain = FileField('XTrain', validators=[FileRequired(), FileAllowed(['csv'], 'CSV Files only!')])
    ytrain = FileField('YTrain', validators=[FileRequired(), FileAllowed(['csv'], 'CSV Files only!')])

class UploadForm(FlaskForm):
    # pickle = FileField('Pickle', validators=[FileRequired(), FileAllowed(['pkl'], 'Pickle Files only!')])
    new_data = FileField('Data', validators=[FileRequired(), FileAllowed(['csv'], 'CSV Files only!')])

# class EnquiryForm(FlaskForm):
#     enquiry_dt = DateField(validators=[InputRequired()])
#     name = StringField('Username',validators=[InputRequired(message=username_required)])
#     gender = RadioField(choices=[('Male','Male'),('Female','Female')])
#     birth_dt = DateField(validators=[InputRequired()])
#     school = SelectField()
#     fathers_name = StringField('Fathers Name')
#     fathers_phone = IntegerField('Fathers Phone Number')
#     fathers_email =
#     mothers_name = 
#     mothers_phone = 
#     mothers_email =

# class PhoneForm(FlaskForm):
#     enquiry_dt = DateField(validators=[InputRequired()])
#     name = StringField('Username',validators=[InputRequired(message=username_required)])
#     gender = RadioField(choices=[('Male','Male'),('Female','Female')])
#     birth_dt = DateField(validators=[InputRequired()])
#     fathers_phone = StringField('Fathers Phone', validators=[DataRequired()])
#     mothers_phone = StringField('Mothers Phone', validators=[DataRequired()])

#     def validate_phone(self, phone):
#         try:
#             p = phonenumbers.parse(phone.data)
#             if not phonenumbers.is_valid_number(p):
#                 raise ValueError()
#         except (phonenumbers.phonenumberutil.NumberParseException, ValueError):
#             raise ValidationError('Invalid phone number')