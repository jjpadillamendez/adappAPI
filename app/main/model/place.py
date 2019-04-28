from .. import db, flask_bcrypt
import datetime
import jwt
from app.main.model.blacklist import BlacklistToken
from ..config import key

class Place(db.Model):
    """ Place Model for storing place related details """
    __tablename__ = "place"

    place_id = db.Column(db.String, nullable=False)
    review = db.Column(db.String(255), nullable=True)
    name = db.Column(db.String(255), nullable=True)
    latitud = db.Column(db.String(255), primary_key=True, nullable=True)
    longitud = db.Column(db.String(255), primary_key=True, nullable=True)
    accessibilities = db.Column(db.String(255), nullable=True)
    rating = db.Column(db.Integer, nullable=True)