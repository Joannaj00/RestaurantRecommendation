from flask import Flask, request, jsonify
# from model.database import db
from controller.Restaurant_controller import get_restaurants
# from model.UserChoice import UserChoice

def map_restaurant_json():
    try:
        # parameters={
        #     'location': request.args.get('location', 'US'),
        #     'term': request.args.get('term', 'restaurants'),
        #     'sort_by': request.args.get('sort_by', 'best_match'),
        #     'limit' : request.args.get('limit', 20)
        # }
        print("!: " ,request.json.get('location', 'US'))
        restaurants = get_restaurants(request.args.get('location', 'US'), 'location')

        # try changing params in the get_restaurants and also fix the email problem 

        # jsonify converts the Python dict to JSON format
        return jsonify(restaurants)
    except Exception as e:
        # 500 is a server error
        return jsonify({'error': str(e)}), 500
    
# def add_favorite_view():    
#     user_id = request.json.get('user_id')
#     restaurant_id = request.json.get('restaurant_id')
#     # link a user to their favorite restaurant.
#     new_favorite = UserChoice(user_id=user_id, restaurant_id=restaurant_id)
#     # adds the new UserChoice to the database and save 
#     # db.session.add(new_favorite)
#     # db.session.commit()
    
#     # 201 stands for "created" 
#     return jsonify({'message': 'Added to favorites'}), 201

# def get_favorite_view(user_id):
#     # retrieve all the favorite restaurants for this user
#     favorites = UserChoice.query.filter_by(user_id=user_id).all()
#     # create a list of dictionaries, each containing restaurant_id and the timestamp when it was added 
#     favorites_list = [{'restaurant_id': fav.restaurant_id, 'picked_at': fav.picked_at} for fav in favorites]
#     return jsonify(favorites_list)