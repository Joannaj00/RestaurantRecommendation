from flask import Flask, request, jsonify
# from model.database import db
from controller.Restaurant_controller import get_restaurants, get_restaurants_helper
# from model.UserChoice import UserChoice

def map_restaurant_json():
    try:
        parameters={
            'location': request.json.get('location', 'US'),
            'categories': request.json.get('categories',''),
            'price': request.json.get('price','')
        }
        restaurants = get_restaurants(parameters)
        # jsonify converts the Python dict to JSON format
        return jsonify(restaurants)
    except Exception as e:
        # 500 is a server error
        return jsonify({'error': str(e)}), 500 

# need a login, when a user joins, we need to know which user is which 
# section saying what is the name or user id 


# def get_favorite_view(user_id):
#     # retrieve all the favorite restaurants for this user
#     favorites = UserChoice.query.filter_by(user_id=user_id).all()
#     # create a list of dictionaries, each containing restaurant_id and the timestamp when it was added 
#     favorites_list = [{'restaurant_id': fav.restaurant_id, 'picked_at': fav.picked_at} for fav in favorites]
#     return jsonify(favorites_list)