from . import db
from werkzeug.security import generate_password_hash

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username=db.Column(db.String(255))
    password=db.Column(db.String(255))
    name=db.Column(db.String(255)) 
    email=db.Column(db.String(255)) 
    location=db.Column(db.String(255)) 
    biography=db.Column(db.String(255)) 
    photo=db.Column(db.String(255))
    date_joined=db.Column(db.DateTime)

    def __init__(self, username, password,name, email, location, biography, photo, date_joined):
        self.username=username
        self.password = generate_password_hash(password, method='pbkdf2:sha256')
        self.name=name
        self.email=email
        self.location=location 
        self.biography=biography
        self.photo=photo
        self.date_joined=date_joined
    
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False
    
    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
    
    def __repr__(self):
        return '<User %r>' % (self.username)
    
    def serialize(self):
        return {
            'id':self.id,
            'username':self.username,
            'name':self.name,
            'photo':self.photo,
            'email':self.email,
            'location':self.location,
            'biography':self.biography,
            'date_joined':self.date_joined
        }


class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    description = db.Column(db.String(1000))
    make = db.Column(db.String(50))
    model = db.Column(db.String(50))
    colour = db.Column(db.String(50))
    year = db.Column(db.String(50))
    transmission = db.Column(db.String(50))
    car_type = db.Column(db.String(50))
    price = db.Column(db.Float)
    photo = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer)

    def __init__(self, description, make, model, colour, year, transmission, car_type, price, photo, userid):
        self.description = description
        self.make = make
        self.model = model
        self.colour = colour
        self.year = year
        self.transmission = transmission
        self.car_type = car_type
        self.price = price
        self.photo = photo
        self.user_id = userid  
    
    def serialize(self):
        return {
            'id':self.id,
            'description':self.description,
            'make':self.make,
            'model':self.model,
            'colour':self.colour,
            'year':self.year,
            'transmission':self.transmission,
            'car_type':self.car_type,
            'price':self.price,
            'photo':self.photo,
            'user_id':self.user_id
        }
   
class Favourites(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True, nullable=False,autoincrement=True)
    car_id = db.Column(db.Integer)
    
    user_id = db.Column(db.Integer)

    def __init__(self, car_id, user_id):
        self.car_id = car_id
        self.user_id = user_id

    def serialize(self):
        return {
            'car_id':self.car_id,
            'user_id':self.user_id
        }
    

        



