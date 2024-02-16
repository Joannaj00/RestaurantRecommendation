# create table about users (user_id) but in the future can add name, bday ... 
from model.database import db

# Define the UserChoice model
class Users(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.String, primary_key=True, nullable=False)
# Create the tables in the database
    def __init__(cls,username):
        cls.username=username 

    @classmethod
    def find_by_username(cls,username):
        return cls.query.filter_by(username=username).count()

# add helper functions to add to the table 
    # db.create_all()