from ..db import db

class Dog(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, unique=True, nullable=False)
    age = db.Column(db.Integer)
    unadopted_image = db.Column(db.String)
    adopted_image = db.Column(db.String)
    adopted = db.Column(db.Boolean)

    def __init__(self, name : str, age : int, unadopted_image : str, \
                 adopted_image : str, adopted : bool) -> None:
        self.name : str = name
        self.age : int = age
        self.unadopted_image : str = unadopted_image
        self.adopted_image : str = adopted_image
        self.adopted : bool = adopted
