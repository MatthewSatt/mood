from flask import Blueprint, jsonify, request
from app.models import db, Moodlist, Song
from flask_login import login_required
from app.forms import AddSongForm, EditSongForm

song_routes = Blueprint("songs", __name__)


# GET ALL SONGS FOR SPECFIC MOOD LIST
@song_routes.route("/moodlists/<int:moodlistId>")
def getMoodlistSongs(moodlistId): # pass in MOODLIST.Id ONLY
    songs = Song.query.filter(Song.moodlistId == moodlistId).all() #id OF MOODLIST
    return jsonify(list(song.to_dict() for song in songs))
    # return jsonify(list(songs.to_dict() for song in songs))



@song_routes.route("/new", methods=['POST'])
def newSong():
    '''
    Passes in object:
    {
            'name': self.name,
            'artist': self.artist,
            'rating': self.rating,
            'song_url': self.song_url,
            'song_image': self.song_image
    }
    '''
    song = request.json

    name = song["name"]
    artist = song["artist"]
    rating = song["rating"]
    song_url = song["song_url"]
    song_image = song["image_url"]
    userId = song["userId"]
    moodlistId = song['moodlistId']
    new_song = Song(name=name, artist=artist, rating=rating, song_url=song_url, song_image=song_image, moodlistId=moodlistId, userId=userId)
    print('NEW SOOOOOOOOOOOOOOOOONG', new_song)
    print(new_song)
    db.session.add(new_song)
    db.session.commit()
    return new_song.to_dict()



# @song_routes.route("edit")
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

@song_routes.route("/delete/<int:songId>", methods=["DELETE"])
def removeSong(songId):
    print('BACKEND SONG ID...............', songId)
    deleted_song = Song.query.filter(Song.id == songId).first()
    print(deleted_song)
    db.session.delete(deleted_song)
    db.session.commit()
    return deleted_song.to_dict()
