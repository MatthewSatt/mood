from app.models import db, Moodlist


def seed_moodlist():
    moodlist1 = Moodlist(
        name='Angry', color='Red', userId=1)
    moodlist2= Moodlist(
        name='Happy', color='Yellow', userId=1)
    moodlist3= Moodlist(
        name='Sad', color='Blue', userId=1)
    # moodlist4=Moodlist(
    #     name='Anxiety', color='Purple', userId=1)
    # moodlist5=Moodlist(
    #     name='Nostalgia', color='Orange', userId=1)
    # moodlist6=Moodlist(
    #     name='Panic', color='Green', userId=1)
    moodlist7=Moodlist(
        name='Sentimental', color='Grey', userId=1)




    db.session.add(moodlist1)
    db.session.add(moodlist2)
    db.session.add(moodlist3)
    # db.session.add(moodlist4)
    # db.session.add(moodlist5)
    # db.session.add(moodlist6)
    db.session.add(moodlist7)
    db.session.commit()

def undo_moodlists():
    db.session.execute('TRUNCATE moodlists RESTART IDENTITY CASCADE;')
    db.session.commit()
