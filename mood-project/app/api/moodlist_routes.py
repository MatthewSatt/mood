from flask import Blueprint, jsonify, request
from app.models import db, Moodlist
from flask_login import login_required

moodlist_routes = Blueprint("moodlists", __name__)



@moodlist_routes.route("/<int:id>")
@login_required
def get_all_moodlists(id):
    "This route will return all fo the moodlists in the database"
    moodlists = Moodlist.query.filter(Moodlist.userId == id).all()#id = current id of the user
    return jsonify(list(mood.to_dict() for mood in moodlists))


@moodlist_routes.route("/new", methods=['POST'])
@login_required
def create_new_moodlist(): # pass in the payload
    mood = request.json['mood']
    # print('MOOOOOOOOOD', mood)
    name = mood["name"]
    color = mood["color"]
    userId = mood["userId"]
    new_moodlist = Moodlist(name=name, color=color, userId=userId)
    db.session.add(new_moodlist)
    db.session.commit()
    print(new_moodlist.to_dict())
    return {"mood": new_moodlist.to_dict()}

@moodlist_routes.route("/edit", methods=["PUT"])
# @login_required
def edit_moodlist():
    '''this route passes in the new moodlist data AND the moodlist id'''
    data = request.json
    obj = data["moodlist"]
    print("........................................NEW", obj)
    moodlist = Moodlist.query.get(obj['id'])
    moodlist.name = obj["name"]
    moodlist.color = obj["color"]
    db.session.commit()

    return { "moodlists": moodlist.to_dict() }

@moodlist_routes.route("/<int:id>/delete", methods=["DELETE"])
@login_required
def delete_moodlist(id):
    deleted_mood = Moodlist.query.filter(Moodlist.id == id).first()
    db.session.delete(deleted_mood)
    db.session.commit()
    return deleted_mood.to_dict()
