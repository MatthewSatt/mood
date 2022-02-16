from flask import Blueprint, jsonify, request
from app.models import db, Moodlist
from flask_login import login_required

moodlist_routes = Blueprint("moodlists", __name__)



@moodlist_routes.route("/")
def get_all_moodlists(id):
    """This route will return all fo the moodlists in the database"""
    moodlists = Moodlist.query.filter(Moodlist.userId == id).all()#id = current id of the user
    return jsonify(list(mood.to_dict() for mood in moodlists))


@moodlist_routes.route("/new", methods=['POST'])
def create_new_moodlist(): # pass in the payload
    incoming = request.json
    name = incoming["name"]
    color = incoming["color"]
    userId = incoming["userId"]
    new_moodlist = Moodlist(name=name, color=color, userId=userId)
    db.session.add(new_moodlist)
    db.session.commit()
    return new_moodlist.to_dict()

@moodlist_routes.route("/edit", methods=["PUT"])
def edit_moodlist():
    '''this route passes in the new moodlist data AND the moodlist id'''
    data = request.json
    id = data["id"]
    moodlist = Moodlist.query.get(id)
    moodlist.name = data["name"]
    moodlist.color = data["color"]

    db.session.commit()
    return {"message": "Successful"}

@moodlist_routes.route("/delete", methods=["DELETE"])
def delete_moodlist():
    '''this route deletes a specific watchlist by passing in the moodlist id'''
    id = request.json['id']
    moodlist = Moodlist.query.get(id)
    db.session.delete(moodlist)
    db.session.commit()
    return moodlist.to_dict()
