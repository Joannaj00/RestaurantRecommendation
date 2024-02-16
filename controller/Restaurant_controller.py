import requests
import os
from nylas import Client
from controller.config.nylas_configs import client
from controller.config.yelp_configs import url, headers 

parameters = {
    'location': 'US',
    'term': 'restaurants',
    'sort_by': 'best_match',
    'limit': 20
}

def get_restaurants_helper(param,key):
    # print(param, key)
    if param!='':
        parameters[key]=param
    response = requests.get(url, params=parameters, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data['businesses']
    else:
        raise Exception("ERROR in status code")

def get_restaurants(params):
    key=['location','categories','price']
    restaurant_list = []
    for i in range(3):
        restaurant_list=get_restaurants_helper(params.get(key[i]), key[i])
    return restaurant_list


def prepare_email_content(restaurants):
    email_content = "Here are your restaurant recommendations:\n\n"
    for idx, restaurant in enumerate(restaurants, 1):
        email_content += f"{idx}. {restaurant['name']}: {restaurant['location']['display_address']}\n \
  rating= {restaurant['rating']}, price= {restaurant['price']}\n\n"
    return email_content
    

def send_email(email, restaurants):
    try:
        # Prepare the email content
        email_content = prepare_email_content(restaurants)
        
        # Validate email format
        if not isinstance(email, str) or '@' not in email or '.' not in email:
            raise ValueError("Invalid email address")

        # Validate email content
        if not isinstance(email_content, str) or len(email_content) == 0:
            raise ValueError("Invalid email content")

        # Validate subject
        subject = "Restaurant Recommendations"
        if not isinstance(subject, str) or len(subject) == 0:
            raise ValueError("Invalid email subject")

        # Send the email
        draft = client.drafts.create()
        draft.subject = subject
        draft.body = email_content
        draft.to = [{'email': email}]
        draft.send()
        print("Restaurant recommendations have been sent")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Welcome to the Restaurant Finder Chatbot!")
    location = input("Please enter the city/state where you want to find restaurants: ")
    restaurants= requests.get(url, params=parameters, headers=headers).json()
    restaurants= get_restaurants_helper(location,'location')
    alias= input("Please enter the type of food you want (ex. vegan, seafood, japanese): ")
    restaurants= get_restaurants_helper(alias,'categories')
    price= input("Please enter the pricing level you want (type 1=$, 2=$$, 3=$$$, 4=$$$$): ")
    restaurants= get_restaurants_helper(price,'price')
    for idx, restaurant in enumerate(restaurants, 1):
        if restaurant.get('price') != None: 
            print(f"{idx}. {restaurant['name']}: {restaurant['location']['display_address']}\n \
  rating= {restaurant['rating']}, price= {restaurant['price']}")
    
    email_choice= input("Do you want to receive the restaurant recommendations via email? (yes/no): ")

    if email_choice== 'yes':
        email=input("Please enter your email address: ")
        if email!= '':
            send_email(email,restaurants)
            print("Restaurant recommendations have been sent to ",email)
        else:
            print("Invalid email address. Email not sent.")
    else:
        print("Restaurant recommendations not sent via email.")


if __name__ == "__main__":
    main()

