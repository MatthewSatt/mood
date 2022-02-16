from app.models.db import db

class Song(db.Model):
    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    artist = db.Column(db.String(40), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    moodlistId = db.Column(db.Integer, db.ForeignKey("moodlists.id"), nullable=False)


    user = db.relationship("User", back_populates="song")
    moodlist= db.relationship("Moodlist", back_populates="song")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'artist': self.artist,
            'rating': self.rating,
            'userId': self.userId,
            'moodlistId': self.moodlistId
        }
