from flask import Blueprint, jsonify, session, request
from app.models import User, Moodlist, Song, db
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required

auth_routes = Blueprint('auth', __name__)


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        return current_user.to_dict()
    return {'errors': ['Unauthorized']}


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            username=form.data['username'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        moodlist_starter1 = Moodlist(
            name='Happy', color='green', userId=user.id)
        moodlist_starter2 = Moodlist(
            name='Sad', color='blue', userId=user.id)
        moodlist_starter3 = Moodlist(
            name='Bored', color='purple', userId=user.id)
        db.session.add(moodlist_starter1)
        db.session.add(moodlist_starter2)
        db.session.add(moodlist_starter3)
        db.session.commit()
        song_starter_one = Song(name="It's Time", artist='Imagine Dragons', rating=10, song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645637061/Imagine_Dragons_-_It_s_Time_Lyrics_e6bv1b.mp3", userId=user.id, moodlistId=moodlist_starter1.id)
        song_starter_two = Song(name='Happy', artist='Pharrell Williams', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1647847521/Pharrell_Williams_-_Happy_HQ__getmp3.pro_snkhpg.mp3", rating=2, userId=user.id, moodlistId=moodlist_starter1.id)
        song_starter_three = Song(name='Nothing Inside', artist='MGK', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635424/Machine_Gun_Kelly_Ft._Iann_Dior_-_nothing_inside_Official_Audio_ksjfxm.mp4', rating=3, userId=user.id, moodlistId=moodlist_starter2.id)
        song_starter_four = Song(name='Demons', artist='Imagine Dragons', rating=9,  song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645635817/Demons_-_Imagine_Dragons_gc5tcu.mp4', userId=user.id, moodlistId=moodlist_starter2.id)
        song_starter_five = Song(name='The Black Parade', artist='MCR', song_url="https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645636620/Welcome_To_The_Black_Parade_-_My_Chemical_Romance_Lyrics_gpfjlu.mp3", rating=8, userId=user.id, moodlistId=moodlist_starter3.id)
        song_starter_six = Song(name='Bored To Death', artist='Blink-182', song_url='https://res.cloudinary.com/matthewsatterwhite/video/upload/v1645634742/blink-182_-_Bored_To_Death_Official_Video_uohps1.mp4', rating=7, userId=user.id, moodlistId=moodlist_starter3.id)
        db.session.add(song_starter_one)
        db.session.add(song_starter_two)
        db.session.add(song_starter_three)
        db.session.add(song_starter_four)
        db.session.add(song_starter_five)
        db.session.add(song_starter_six)
        db.session.commit()
        login_user(user)
        return user.to_dict()
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
