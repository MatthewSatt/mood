from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from app.models import Moodlist
from wtforms.validators import DataRequired, ValidationError


class AddMoodForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()])
    color = StringField('color')
    userId = IntegerField('userId')
    submit = SubmitField('submit')
