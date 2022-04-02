from wsgiref.validate import validator
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired



class AddSongForm(FlaskForm):
    name = StringField("name", validators=[DataRequired("Please provide a name for the song.")])
    artist = StringField("artist", validators=[DataRequired("Please provide a name for the artist")])
    rating = IntegerField("rating", validators=[DataRequired("Please provide a rating for the song")])
    song_url = StringField("song_url")
    song_image = StringField("song_image")
    userId = IntegerField("userId", validators=[DataRequired()])
    moodlistId = IntegerField("moodlistId", validators=[DataRequired()])
    submit = SubmitField("submit")
