from flask import Flask, request, jsonify
# from model.database import db
import view.Restaurant_view as Restaurant_view
# from model.UserChoice import UserChoice

app = Flask(__name__)
# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

## ENDPOINTS GO HERE 

#Getting restaurants from yelp
@app.route('/restaurants', methods=['GET','POST'])
def get_restaurants():
    return Restaurant_view.map_restaurant_json()

# #Adding to the user list of favorites
# @app.route('/add_favorite/<int:user_id>/<int:restaurant_id>', methods=['POST'])
# def add_favorite():
#     Restaurant_view.add_favorite_view()

# #Getting list of user favorites
# @app.route('/favorites/<int:user_id>', methods=['GET'])
# def get_favorites(user_id):
#     Restaurant_view.get_favorite_view(user_id)
    
# # dummy 
# @app.route("/hello") 
# def hello(): 
#     return "hi!"

# control c to exit