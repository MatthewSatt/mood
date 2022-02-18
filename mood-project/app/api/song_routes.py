from flask import Blueprint, jsonify, request
from app.models import db, Moodlist, Song
from flask_login import login_required
from app.forms import AddSongForm, EditSongForm

song_routes = Blueprint("songs", __name__)


# GET ALL SONGS FOR SPECFIC MOOD LIST
@song_routes.route("/")
def getMoodlistSongs(): # pass in MOODLIST.Id ONLY
    id = 1
    songs = Song.query.filter(Song.moodlistId == id).all() #id OF MOODLIST
    return jsonify(list(song.to_dict() for song in songs))
    # return jsonify(list(songs.to_dict() for song in songs))



@song_routes.route("/new", methods=['POST'])
def newSong():
    '''
    Passes in object:
    {
    "name": "Matthew",
    "artist": "Satterwhite",
    "rating": 10,
    "userId": 1,
    "moodlistId": 1
}
    '''
    song = request.json
    print(song)
    name = song["name"]
    artist = song["artist"]
    rating = song["rating"]
    userId = song["userId"]
    moodlistId = song["moodlistId"]
    new_song = Song(name=name, artist=artist, rating=rating, userId=userId, moodlistId=moodlistId)
    db.session.add(new_song)
    db.session.commit()
    return {"song": new_song.to_dict()}



# @song_routes.route("/edit")
# def changeSong():
#         '''
#         Passes in Song.Id

#         '''
#         data = request.json
#         # form = EditSongForm()
#         current_song = Song.query.get(id)
#         current_song.body = data['body']
#         # data.form['body']

#         db.session.commit()
#         return current_song.to_dict()
