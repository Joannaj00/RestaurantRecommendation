from model.Users_model import Users 
from model.database import db

def user_signup(username):
    print("hi")
    if Users.find_by_username(username)==0:
        user= Users(username)
        db.session.add(user)
        db.session.commit()
        print(Users.find_by_username(username))
        return ""
    else:
        return "Username taken"
