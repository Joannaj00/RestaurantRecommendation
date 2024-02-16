from model.database import db
import controller.Restaurant_controller as Restaurant
from datetime import datetime

# Define the UserChoice model
class UserChoice(db.Model):
    __tablename__ = 'user_choices'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    picked_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserChoice {self.user_id} - {self.restaurant_id}>'

    def __init__(self,id,username,restaurant_id, picked_at):
        self.id=id
        self.username=username
        self.restaurant_id=restaurant_id
        self.picked_at=picked_at
    
    @classmethod
    def find_restaurant(cls, username, restaurant_id):
        return cls.query.filter_by(username=username, restaurant_id=restaurant_id, vertified=True).count()
        

    # Class method to add a user's restaurant pick
    @classmethod
    def add_user_pick(cls, username, restaurant_id):
        new_pick = cls(username=username, restaurant_id=restaurant_id)
        db.session.add(new_pick)
        db.session.commit()

    # Class method to get the top restaurants based on picks
    @classmethod
    def get_top_picks(cls):
        return db.session.query(
            Restaurant.name,
            Restaurant.city,
            Restaurant.cuisine_type,
            Restaurant.price_range,
            db.func.count(cls.id).label('total_picks')
        ).join(Restaurant).group_by(Restaurant.id).order_by(db.desc('total_picks')).all()

    # Class method to get user's favorite choices
    @classmethod
    def get_user_favorites(cls, username):
        return cls.query.filter_by(username=username).join(Restaurant).order_by(cls.picked_at.desc()).all()

# Create the tables in the database
db.create_all()