import os
import sys
import unittest
import datetime
import uuid

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager, Command

from app.main import create_app, db
from app.main.model.user import User
from app.main.model.place import Place
from app import blueprint

class FlagManager(Manager):
    def command(self, capture_all=False):
        def decorator(func):
            command = Command(func)
            command.capture_all_args = capture_all
            self.add_command(func.__name__, command)

            return func
        return decorator

app = create_app(os.getenv('BOILERPLATE_ENV') or 'dev')
app.register_blueprint(blueprint)
app.app_context().push()
manager = FlagManager(app)
migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command()
def run():
    app.run(host='0.0.0.0', port=80)

@manager.command()
def test():
    """Runs the unit tests."""
    tests = unittest.TestLoader().discover('app/test', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1

@manager.command(True)
def create_admin(*args):

    if len(args[0]) < 2:
        print("Usage: python manage.py create_admin [user] [password] ")

    admin = User(
            public_id=str(uuid.uuid4()),
            email="admin",
            username=sys.argv[2],
            password=sys.argv[3],
            admin= True,
            registered_on=datetime.datetime.utcnow()
        )
    place1 = Place(
        review = "The Service was Amazing, The Disability Help Group got my Disability for Cancer through in only 4 months! Every time I called and spoke to a representative I was treated with courtesy and respect, I plan to refer them to anyone I meet going through the same situation. KEEP up the good work !!",
        name = "Whataburger",
        latitud = "31.773807",
        longitud = "-106.500575",
        place_id = "31.773807.-106.500575",
        rating = 2
    )
    place2 = Place(
        review = "We used to frequent this restaurant often. However, as my Husband's mobility has worsened, we are unable to re- visit, as its not Disabled friendly. The food and staff were lovely. Needed is a ground floor toilet and better ramp access",
        name = "The Pizza Joint",
        latitud = "31.779147",
        longitud = "-106.504197",
        place_id = "31.779147.-106.504197",
        rating = 1
    )
    place3 = Place(
        review = "I found a ramp here :)",
        name = "ramp",
        latitud = "31.771851",
        longitud = "-106.504694",
        place_id = "31.771851.-106.504694",
        rating = 5
    )
    db.session.add(place1)  
    db.session.add(place2)  
    db.session.add(place3)
    db.session.commit()
    
    db.session.add(admin)   
    db.session.commit()

@manager.command(True)
def create_mongodb_collections(*args):
    mongo.db.createCollection('places')

if __name__ == '__main__':
    # Command.capture_all_args = True
    manager.run()

