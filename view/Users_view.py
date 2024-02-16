from flask import Flask, request, jsonify
# from model.database import db
from controller.Users_controller import user_signup

# def signup():
#     if request.is_json:
#         print("users_view")
#         username= request.json.get('username')
#         user = user_signup(username)
#         if user == "":
#             return jsonify({"message": "Signup successful!"}), 200
#         else:
#             return jsonify({"error": "Username taken"}), 400
#     else:
#         return jsonify({"error": "Request must be JSON"}), 400

def signup():
    return jsonify({"message": "This is a test response"}), 200