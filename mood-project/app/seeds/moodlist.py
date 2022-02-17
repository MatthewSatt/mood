from app.models import db, Moodlist


def seed_moodlist():
    moodlist1= Moodlist(
        name='Happy1', color='Yellow', userId=1)
    moodlist2 = Moodlist(
        name='Mad1', color='Red', userId=1)
    moodlist3= Moodlist(
        name='Sad1', color='Blue', userId=1)
    moodlist4= Moodlist(
        name='Happy2', color='Orange', userId=1)
    moodlist5 = Moodlist(
        name='Mad2', color='Green', userId=1)
    moodlist6= Moodlist(
        name='Sad2', color='Pink', userId=1)
    moodlist7= Moodlist(
        name='Happy3', color='Silver', userId=1)
    moodlist8 = Moodlist(
        name='Mad3', color='White', userId=1)
    moodlist9= Moodlist(
        name='Sad3', color='Purple', userId=1)
    moodlist10= Moodlist(
        name='Happy3', color='Brown', userId=1)
    moodlist11 = Moodlist(
        name='Mad4', color='Balck', userId=1)
    moodlist12= Moodlist(
        name='Sad4', color='Tan', userId=1)
    moodlist13= Moodlist(
        name='Happy4', color='Green', userId=1)
    moodlist13 = Moodlist(
        name='Mad5', color='Red', userId=1)
    moodlist14= Moodlist(
        name='Sad5', color='White', userId=1)


    moodlist7=Moodlist(
        name='Sentimental', color='Grey', userId=1)




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
    db.session.commit()

def undo_moodlists():
    db.session.execute('TRUNCATE moodlists RESTART IDENTITY CASCADE;')
    db.session.commit()
