from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class EditSongForm(FlaskForm):
    name = StringField("name", validators=[DataRequired("Please provide a name for the song.")])
    artist = StringField("artist", validators=[DataRequired("Please provide a name for the artist")])
    rating= IntegerField("rating", validator=[DataRequired("Please prove a rating for the song")])
    submit = SubmitField("submit")
