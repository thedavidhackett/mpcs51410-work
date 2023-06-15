from typing import List
from ..db import db
from ..model.dog import Dog

from flask import Blueprint, render_template

bp = Blueprint('/', __name__, url_prefix='/')

@bp.route("")
def home():
    dogs : List[Dog] = Dog.query.all()
    return render_template("home.html", dogs=dogs)

@bp.get("/<id>")
def dog_get(id=None):
    dog : Dog = db.get_or_404(Dog, id)
    return render_template("dog.html", dog=dog)

@bp.post("/<id>")
def dog_post(id=None):
    dog : Dog = db.get_or_404(Dog, id)
    dog.adopted = True
    db.session.commit()
    return render_template("dog.html", dog=dog)
