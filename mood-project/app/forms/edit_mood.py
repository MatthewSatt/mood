from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



class EditMoodForm(FlaskForm):
    name = StringField('name', validators=[DataRequired("Please provide a name the Playlist.")])
    body = StringField('color')
    submit = SubmitField('submit')
