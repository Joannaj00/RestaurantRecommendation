from flask import Flask, request, jsonify
from model.database import db
import view.Restaurant_view as Restaurant_view
import view.Users_view as Users_view
from flask_migrate import Migrate
from flask_cors import CORS
from flask_socketio import SocketIO

app = Flask(__name__)

# # Allow CORS for all domains on all routes
# CORS(app, resources={r"/*": {"origins": "*"}})  # Adjusted to explicitly allow all origins

socketio = SocketIO(app, cors_allowed_origins="*")

### CORS section
@app.after_request
def after_request_func(response):
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                            'GET, POST, OPTIONS, PUT, PATCH, DELETE')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        if origin:
            response.headers.add('Access-Control-Allow-Origin', origin)

    return response
### end CORS section

# Configure the SQLAlchemy part of the app instance
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)

db.init_app(app)

## ENDPOINTS GO HERE 

#Getting restaurants from yelp
@app.route('/restaurants', methods=['GET','POST'])
def get_restaurants():
    return Restaurant_view.map_restaurant_json()

@app.route('/login',methods=['POST',"OPTION"])
def get_login():
    print("App.py")
    return Users_view.signup()

# @app.route('/get_user',methods=['POST'])


#Adding to the user list of favorites
# # users are in my database, when a user favorites a restaurant, I will add that to userchoice (user id, restaurant)
@app.route('/add_favorite/<int:username>/<int:restaurant_id>', methods=['POST'])
def add_favorite():
    Restaurant_view.add_favorite_view(username, restaurant_id)

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
    CORS(app)

    with app.app_context():
        db.create_all()
    socketio.run(app, port=5002)
    app.run(port=5000)
