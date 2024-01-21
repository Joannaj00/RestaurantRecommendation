from flask import Flask, request, jsonify
from controller.Restaurant_controller import 
from model.UserChoice_model import UserChoice 


def add_favorite():    
    username = request.json.get('username')
    restaurant_id = request.json.get('restaurant_id')
    # link a user to their favorite restaurant.
    new_favorite = UserChoice(username=username, restaurant_id=restaurant_id)
    # adds the new UserChoice to the database and save 
    # db.session.add(new_favorite)
    # db.session.commit()

    # 201 stands for "created" 
    return jsonify({'message': 'Added to favorites'}), 201
