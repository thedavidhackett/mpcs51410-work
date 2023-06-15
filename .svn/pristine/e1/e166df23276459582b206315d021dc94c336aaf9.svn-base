from flask import Flask
from .controller import dog_controller
from .db import db
from .model.dog import Dog


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)

with app.app_context():
    db.drop_all()
    db.create_all()

    dog : Dog = Dog("Ozzie", 5, "ozzie_sad.jpg", "ozzie_happy.jpg", False)

    db.session.add(dog)
    db.session.commit()

app.register_blueprint(dog_controller.bp)
