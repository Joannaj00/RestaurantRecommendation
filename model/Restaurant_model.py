from database import db

# Define the Restaurant model
class Restaurant(db.Model):
    __tablename__ = 'restaurants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    city = db.Column(db.String(50), nullable=False)
    cuisine_type = db.Column(db.String(50))
    price_range = db.Column(db.String(10))

    # Create a relationship to UserChoices
    user_choices = db.relationship('UserChoice', backref='restaurant', lazy=True)

    def __repr__(self):
        return f'<Restaurant {self.name}>'