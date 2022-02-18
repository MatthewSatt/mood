from app.models import db, Moodlist


def seed_moodlist():
    moodlist1= Moodlist(
        name='Aggressive', color='Yellow', userId=1)
    moodlist2 = Moodlist(
        name='Confident', color='Red', userId=1)
    moodlist3= Moodlist(
        name='Gentle', color='Blue', userId=1)
    moodlist4= Moodlist(
        name='Epic', color='Orange', userId=1)
    moodlist5 = Moodlist(
        name='Dramatic', color='Green', userId=1)
    moodlist6= Moodlist(
        name='Relaxed', color='Pink', userId=1)
    moodlist7= Moodlist(
        name='Nostalgic', color='Silver', userId=1)
    moodlist8 = Moodlist(
        name='Melodic', color='White', userId=1)
    moodlist9= Moodlist(
        name='Meditative', color='Purple', userId=1)
    moodlist10= Moodlist(
        name='Gloomy', color='Brown', userId=1)
    moodlist11 = Moodlist(
        name='Driving', color='Black', userId=1)
    moodlist12= Moodlist(
        name='Sad', color='Tan', userId=1)
    moodlist13= Moodlist(
        name='Happy', color='Green', userId=1)
    moodlist14 = Moodlist(
        name='Scary', color='Red', userId=1)
    moodlist15= Moodlist(
        name='Annoyed', color='White', userId=1)




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
