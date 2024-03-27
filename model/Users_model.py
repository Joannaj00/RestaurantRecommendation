# create table about users (user_id) but in the future can add name, bday ... 
from model.database import db

# Define the UserChoice model
class Users(db.Model):
    __tablename__ = 'users'
    # id = db.Column(db.Integer, )
    username = db.Column(db.String(10), primary_key=True)
# Create the tables in the database
    def __init__(self,username):
        self.username=username 

    @classmethod
    def find_by_username(self,username):
        print("inside")
        return self.query.filter_by(username=username).count()


# add helper functions to add to the table 
    # db.create_all()