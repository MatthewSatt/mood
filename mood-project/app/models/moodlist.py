from app.models.db import db


from app.models.db import db

class Moodlist(db.Model):
    __tablename__ = 'moodlists'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False, unique=True)
    color = db.Column(db.String(40))
    userId = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    user = db.relationship("User", back_populates="moodlist")
    song = db.relationship("Song", back_populates="moodlist")

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'color': self.color,
            "userId": self.userId
        }
