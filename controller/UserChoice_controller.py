from model.UserChoice_model import UserChoice 
from model.database import db

def add_favorite(username,restaurant_id):
    if UserChoice.find_restaurant(username,restaurant_id)==0:
        new_favorite = UserChoice(username=username, restaurant_id=restaurant_id)
        db.session.add(new_favorite)
        db.session.commit()
        return ""
    else:
        return "Restaurant already in the list"
