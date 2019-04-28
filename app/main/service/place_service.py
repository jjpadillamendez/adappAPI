import uuid
import datetime

from app.main import db
from app.main.model.place import Place
from sqlalchemy import or_

def get_all_places():
    return Place.query.all()

def delete_place(latitud, longitud):
    place_id = "{}.{}".format(latitud, longitud)
    if Place.query.filter_by(place_id=place_id).delete():
        db.session.commit()
        response_object = {
            'status': 'sucess',
            'message': 'Place was deleted',
        }
        return response_object, 200
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place does not exit. Please try another place id',
        }
        return response_object, 409

def update_place(data):
    placed_id = "{}.{}".format(data['latitud'], data['longitud'])
    place = Place.query.filter(or_(Place.place_id == placed_id)).first()
    if place:
        place.name = data['name']
        place.review = data['review']
        place.rating = data['rating']
        place.accessibilities = data['accessibilities']

        response_object = {
            'status': 'success',
            'message': 'Place was updated',
        }
      
        db.session.commit()
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place does not exist. Please select a valid place.',
        }
        return response_object, 409

def save_new_place(data):
    placed_id = "{}.{}".format(data['latitud'], data['longitud'])
    place = Place.query.filter(or_(Place.place_id == placed_id)).first()
    if not place:
        new_place = Place(
            place_id=placed_id,
            name=data['name'],
            review=data['review'],
            rating=data['rating'],
            longitud=data['longitud'],
            latitud=data['latitud'],
            accessibilities = data['accessibilities']
        )
        response_object = {
            'status': 'sucess',
            'message': 'Place was created',
        }
        db.session.add(new_place)
        db.session.commit()
        return response_object, 201
    else:
        response_object = {
            'status': 'fail',
            'message': 'Place already exists. Please add another one.',
        }
        return response_object, 409

def get_a_place(latitud, logitud):
    place_id = "{}.{}".format(latitud, logitud)
    return Place.query.filter_by(place_id=place_id).first()