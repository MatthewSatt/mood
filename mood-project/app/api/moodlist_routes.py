from flask import Blueprint, jsonify, request
from app.models import db, Moodlist
from flask_login import login_required
from app.forms import AddMoodForm, EditMoodForm

moodlist_routes = Blueprint("moodlists", __name__)

def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f'{field} : {error}')
    return errorMessages


@moodlist_routes.route("/<int:id>")
@login_required
def get_all_moodlists(id):
    "This route will return all fo the moodlists in the database"
    moodlists = Moodlist.query.filter(Moodlist.userId == id).all()#id = current id of the user
    return jsonify(list(mood.to_dict() for mood in moodlists))


@moodlist_routes.route("/new", methods=['POST'])
@login_required
def create_new_moodlist(): # pass in the payload
    # data = request.json
    form = AddMoodForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        name = form.data["name"]
        color = form.data["color"]
        userId = form.data["userId"]
        new_moodlist = Moodlist(name=name, color=color, userId=userId)
        db.session.add(new_moodlist)
        db.session.commit()
        return {"mood": new_moodlist.to_dict()}
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401

@moodlist_routes.route("/edit", methods=["PUT"])
# @login_required
def edit_moodlist():
    '''this route passes in the new moodlist data AND the moodlist id'''
    data = request.json
    form = EditMoodForm()
    moodlist = Moodlist.query.get(data['id'])
    # print('.......................................', moodlist.to_dict())
    moodlist.name = data['name']
    moodlist.color = data['color']
    db.session.commit()
    # print('..................................................', moodlist)

    return moodlist.to_dict()

@moodlist_routes.route("/<int:id>/delete", methods=["DELETE"])
@login_required
def delete_moodlist(id):
    deleted_mood = Moodlist.query.filter(Moodlist.id == id).first()
    db.session.delete(deleted_mood)
    db.session.commit()
    return deleted_mood.to_dict()
