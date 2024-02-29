# contains database models and interactions via SQLAlchemy
# local import for db access
from config import db

# db model as a python class for definition
class Contact(db.Model):
    # Unique key for id
    id = db.Column(db.Integer, primary_key=True)
    # String max length, non-unique, non-null values
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    # unique email addresses
    email = db.Column(db.String(100), unique=True, nullable=False)

    # convert fields to a python dictionary, then to JSON for API interaction
    # for object creation
    # JSON: Camel Case, Python: Snake Case
    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
        }