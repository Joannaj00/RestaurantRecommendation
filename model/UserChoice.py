from model.database import db
import controller.Restaurant_controller as Restaurant
from datetime import datetime

# Define the UserChoice model
class UserChoice(db.Model):
    __tablename__ = 'user_choices'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurants.id'), nullable=False)
    picked_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<UserChoice {self.user_id} - {self.restaurant_id}>'

    # Class method to add a user's restaurant pick
    @classmethod
    def add_user_pick(cls, user_id, restaurant_id):
        new_pick = cls(user_id=user_id, restaurant_id=restaurant_id)
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
    def get_user_favorites(cls, user_id):
        return cls.query.filter_by(user_id=user_id).join(Restaurant).order_by(cls.picked_at.desc()).all()

# Create the tables in the database
db.create_all()