from flask_restplus import Namespace, fields


class PlaceDto:
    api = Namespace('place', description='place related operations')
    place = api.model('place', {
        'name' : fields.String(description='name of the place'),
        'place_id' : fields.String(description='unique place identifier'),
        'review' : fields.String(description='place review'),
        'rating' : fields.Integer(description='place rating'),
        'longitud' : fields.String(description='place longitud'),
        'latitud' : fields.String(description='place latitud'),
        'accessibilities' : fields.String(description='place review')
    })

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'public_id': fields.String(description='user Identifier')
    })

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'email': fields.String(required=True, description='The email address'),
        'password': fields.String(required=True, description='The user password '),
    })
