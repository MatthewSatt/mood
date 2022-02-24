from app.models import db, Moodlist


def seed_moodlist():
    moodlist1= Moodlist(
        name='Sample Songs', color='red', userId=1)
    moodlist2 = Moodlist(
        name='Happy', color='green', userId=1)
    moodlist3= Moodlist(
        name='Sad', color='blue', userId=1)
    moodlist4= Moodlist(
        name='Bored', color='purple', userId=1)
    moodlist5 = Moodlist(
        name='Dramatic', color='black', userId=1)
    moodlist6= Moodlist(
        name='Relaxed', color='red', userId=1)
    moodlist7= Moodlist(
        name='Nostalgic', color='green', userId=1)
    moodlist8 = Moodlist(
        name='Melodic', color='blue', userId=1)
    moodlist9= Moodlist(
        name='Meditative', color='purple', userId=1)
    moodlist10= Moodlist(
        name='Gloomy', color='black', userId=1)
    moodlist11 = Moodlist(
        name='Driving', color='brown', userId=1)
    moodlist12= Moodlist(
        name='Gentle', color='red', userId=1)
    moodlist13= Moodlist(
        name='Epic', color='green', userId=1)
    moodlist14 = Moodlist(
        name='Scary', color='blue', userId=1)
    moodlist15= Moodlist(
        name='Annoyed', color='purple', userId=1)




    db.session.add(moodlist1)
    db.session.add(moodlist2)
    db.session.add(moodlist3)
    db.session.add(moodlist4)
    db.session.add(moodlist5)
    db.session.add(moodlist6)
    db.session.add(moodlist7)
    db.session.add(moodlist8)
    db.session.add(moodlist9)
    db.session.add(moodlist10)
    db.session.add(moodlist11)
    db.session.add(moodlist12)
    db.session.add(moodlist13)
    db.session.add(moodlist14)
    db.session.add(moodlist15)
    db.session.commit()

def undo_moodlists():
    db.session.execute('TRUNCATE moodlists RESTART IDENTITY CASCADE;')
    db.session.commit()
