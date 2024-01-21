from flask import Flask, request, jsonify
# from model.database import db
from controller.Users_controller import signup

def signup():
    print("users_view")
    # get username from the frontend
    username= request.json.get('username')
    # parameters={
    #     'username': request.json.get('username')
    # }
    user = signup(username)
    # if user is not "", username is taken 
    if user!="":
        return jsonify(user)
    else:
        return "success!"