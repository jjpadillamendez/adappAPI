from flask import request
from flask_restplus import Resource
from ..util.dto import PlaceDto
from ..service.place_service import get_all_places, save_new_place, get_a_place, delete_place, update_place
from ..util.decorator import token_required, admin_token_required
api = PlaceDto.api
_place = PlaceDto.place

@api.route('/')
class PlaceList(Resource):
    @api.doc('list of registered places')
    @api.marshal_list_with(_place, envelope='data')
    #@token_required
    def get(self):
        """List all registered places"""
        return get_all_places()

    @api.response(201, 'Place successfully added.')
    @api.doc('add a new place')
    @api.expect(_place, validate=True)
    #@token_required
    def post(self):
         """Creates a new Place """
         data = request.json
         return save_new_place(data=data)

    @api.response(200, 'Place successfully updated.')
    @api.doc('update a specific place')
    @api.expect(_place, validate=True)
    def put(self):
        """ update a specific place """
        data = request.json
        return update_place(data)

@api.route('/<latitud>/<longitud>')
@api.param('latitud', 'place latitud')
@api.param('longitud', 'place longitud')
@api.response(404, 'Place not found.')
class Place(Resource):
    @api.doc('get a specific place')
    @api.marshal_with(_place)
    #@admin_token_required
    def get(self, latitud, longitud):
        """get a place given its identifier"""
        place = get_a_place(latitud, longitud)
        if not place:
            api.abort(404)
        else:
            return place

    @api.response(200, 'Place successfully removed.')
    @api.doc('delete a specific place')
    def delete(self, latitud, longitud):
        """ delete a specific place """
        return delete_place(latitud, longitud)