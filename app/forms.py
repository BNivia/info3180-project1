from flask_wtf import FlaskForm
from wtforms import  StringField, TextAreaField, SelectField
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import DataRequired

class NewProperty(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    beds = StringField('No. of Bedrooms', validators=[DataRequired()])
    baths = StringField('No. of Bathrooms', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    ptype = SelectField('Property Type', choices=[("apt", "Apartment"), ("hse","House")])
    img = FileField('Photo', validators=[FileRequired(), FileAllowed(['jpg', 'png', 'Images only!'])])