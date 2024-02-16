from flask import Flask, request, jsonify
from model.database import db
import view.Restaurant_view as Restaurant_view
import view.Users_view as Users_view
# from model.UserChoice import UserChoice

app = Flask(__name__)
# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

## ENDPOINTS GO HERE 

#Getting restaurants from yelp
@app.route('/restaurants', methods=['GET','POST'])
def get_restaurants():
    return Restaurant_view.map_restaurant_json()

@app.route('/login',methods=['POST'])
def get_login():
    print("App.py")
    return Users_view.signup()

# @app.route('/get_user',methods=['POST'])


#Adding to the user list of favorites
# # users are in my database, when a user favorites a restaurant, I will add that to userchoice (user id, restaurant)
# @app.route('/add_favorite/<int:username>/<int:restaurant_id>', methods=['POST'])
# def add_favorite():
#     Restaurant_view.add_favorite_view()

# #Getting list of user favorites
# @app.route('/favorites/<int:user_id>', methods=['GET'])
# def get_favorites(user_id):
#     Restaurant_view.get_favorite_view(user_id)
    
# dummy 
@app.route("/hello") 
def hello(): 
    return "hi!"

# control c to exit
if __name__=="__main__":
    with app.app_context():
        db.create_all()