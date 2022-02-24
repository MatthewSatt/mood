from flask import Blueprint, jsonify, request
from app.models import db, Moodlist, Song
from flask_login import login_required
from app.forms import AddSongForm, EditSongForm

song_routes = Blueprint("songs", __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages

# GET ALL SONGS FOR SPECFIC MOOD LIST
@song_routes.route("/moodlists/<int:moodlistId>")
def getMoodlistSongs(moodlistId): # pass in MOODLIST.Id ONLY
    songs = Song.query.filter(Song.moodlistId == moodlistId).all() #id OF MOODLIST
    return jsonify(list(song.to_dict() for song in songs))
    # return jsonify(list(songs.to_dict() for song in songs))



@song_routes.route("/new", methods=['POST'])
def newSong():
    form = AddSongForm()
    form['csrf_token'].data = request.cookies['csrf_token']


    if form.validate_on_submit():
        name = form.data["name"]
        artist = form.data["artist"]
        rating = form.data["rating"]
        song_url = form.data["song_url"]
        userId = form.data["userId"]
        moodlistId = form.data['moodlistId']
        new_song = Song(name=name, artist=artist, rating=rating, song_url=song_url, moodlistId=moodlistId, userId=userId)
        print(new_song)
        db.session.add(new_song)
        db.session.commit()
        return new_song.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401



@song_routes.route("/edit", methods=["PUT"])
def changeSong():
    data = request.json
    song = Song.query.get(data['id'])
    song.name = data['name']
    song.artist = data['artist']
    song.rating = data['rating']
    # song.song_url = data['song_url']
    # song.song_image = data['image_url']
    song.userId = data['userId']
    song.moodlistId = data['moodlistId']
    db.session.commit()

    return song.to_dict()


@song_routes.route("/delete/<int:songId>", methods=["DELETE"])
def removeSong(songId):
    deleted_song = Song.query.filter(Song.id == songId).first()
    print(deleted_song)
    db.session.delete(deleted_song)
    db.session.commit()
    return deleted_song.to_dict()




@song_routes.route("/play/<int:songId>")
def playSong(songId):
    song = Song.query.filter(Song.id == songId).first()
    print('SONNGGGGGGGGGGGGGGGG', song.to_dict())
    return song.to_dict()
