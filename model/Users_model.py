# create table about users (user_id) but in the future can add name, bday ... 
from model.database import db

# Define the UserChoice model
class Users(db.Model):
    __tablename__ = 'users'
    username = db.Column(db.Integer, primary_key=True, nullable=False)
# Create the tables in the database
    def __init__(self,username):
        self.username=username 

    def find_by_username(self,username):
        return self.query.filter_by(username=username, vertified=True).count()

# add helper functions to add to the table 
    # db.create_all()