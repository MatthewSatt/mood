from app.models import db, Song


def seed_songs():
    song1 = Song(
         name='California', artist='Blink-182', rating=7, userId=1, moodlistId=1)
    song2 = Song(
         name='Hells Bells', artist='ACDC', rating=3, userId=1, moodlistId=1)
    song3 = Song(
        name='Demons', artist='Imagine Dragons', rating=9, userId=1, moodlistId=1)
    song4 = Song(
        name='Despacito', artist='Luis Fonsi', rating=2, userId=1, moodlistId=1)
    song5 = Song(
        name='Bohemian Rhapsody', artist='Queen', rating=8, userId=1, moodlistId=1)
    song6 = Song(
        name='Billy Jean', artist='Micheal Jackson', rating=2, userId=1, moodlistId=1)
    song7 = Song(
        name='Rolling in the deep', artist='Adele', rating=2, userId=1, moodlistId=1)
    song8 = Song(
        name='Somebody that I Used to Know', artist='Gotye', rating=2, userId=1, moodlistId=1)

    db.session.add(song1)
    db.session.add(song2)
    db.session.add(song3)
    db.session.add(song4)
    db.session.add(song5)
    db.session.add(song6)
    db.session.add(song7)
    db.session.add(song8)
    db.session.commit()

def undo_seeds():
    db.session.execute('TRUNCATE songs RESTART IDENTITY CASCADE;')
    db.session.commit()
