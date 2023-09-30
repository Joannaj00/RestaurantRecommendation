import requests
import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail, Email, Personalization, Content
from nylas import APIClient

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer 18QXoPrlSCZvnYYdZSu9NqhuPJcdiGCZ-UuSVc-BRggFFCts7mmiK0xl4k7B6u-7Gq2Cm1FsIUetoEt-hggqofz7K0cKhVsRfyVsdB-nrY70giJvJ7QPcA91JhsWZXYx"
}

parameters = {
    'location': 'US',
    'term': 'restaurants',
    'sort_by': 'best_match',
    'limit': 20
}


def get_restaurants(param,key):
    parameters[key]=param
    # print(parameters)
    response = requests.get(url, params=parameters, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # print(response.url)
        return data['businesses']
    else:
        return None
    

def send_email(email, restaurants):
    client = APIClient(
        '99us5r7lv96v5j9qdb9svs0qc',
        'ajw1eultildosewrrs5a6mu0s',
        '231DJdHWSqMuEXhOsNwvjpXtdIxlu5'
    )
    
    # Prepare the email content
    email_content = "Here are your restaurant recommendations:\n\n"
    for idx, restaurant in enumerate(restaurants, 1):
        email_content += f"{idx}. {restaurant['name']}: {restaurant['location']['display_address']}\n \
  rating= {restaurant['rating']}, price= {restaurant['price']}\n\n"
    
    # message = {
    #     'to': [{'email': email}],
    #     'subject': 'Restaurant Recommendations',
    #     'body': email_content
    # }
    
    # Send the email

    draft=client.drafts.create()
    draft.subject= "Restaurant Recommendations"
    draft.body=email_content
    draft.to=[{'email': email}]

    # draft = client.drafts.create(**message)
    draft.send()
    print(f"Restaurant recommendations has been sent")

def main():
    print("Welcome to the Restaurant Finder Chatbot!")
    location = input("Please enter the city/state where you want to find restaurants: ")
    restaurants= requests.get(url, params=parameters, headers=headers).json()
    if location != '':
        restaurants= get_restaurants(location,'location')
    alias= input("Please enter the type of food you want (ex. vegan, seafood, japanese): ")
    if alias != '':
        restaurants= get_restaurants(alias,'categories')
    price= input("Please enter the pricing level you want (type 1=$, 2=$$, 3=$$$, 4=$$$$): ")
    if price != '':
        # print(price)
        restaurants= get_restaurants(price,'price')
    # print(restaurants)
    for idx, restaurant in enumerate(restaurants, 1):
        if restaurant.get('price') != None: 
            print(f"{idx}. {restaurant['name']}: {restaurant['location']['display_address']}\n \
  rating= {restaurant['rating']}, price= {restaurant['price']}")
    
    email_choice= input("Do you want to receive the restaurant recommendations via email? (yes/no): ")

    if email_choice== 'yes':
        email=input("Please enter your email address: ")
        if email!= '':
            send_email(email,restaurants)
            print("Restaurant recommendations have been sent to {email}")
        else:
            print("Invalid email address. Email not sent.")
    else:
        print("Restaurant recommendations not sent via email.")


if __name__ == "__main__":
    main()


# business_data= response.json()

# print(business_data.keys())

#print(response.text)

# def get_restaurants(location):
#     # response = requests.get(url, headers=headers)
#     # if response.status_code == 200:
#     #     data = response.json()
#     #     return data['businesses']
#     # else:
#     #     return None

#     params = {
#     "location": location,
#     "term": "restaurants",
#     "sort_by": "best_match",
#     "limit": 20
#     }

#     # if price_range:
#     #     params["price"] = price_range

#     # if category:
#     #     params["categories"] = category

#     response = requests.get(url, headers=headers, params=params)

#     if response.status_code == 200:
#         data = response.json()
#         for business in data['businesses']:
#             print(business['name'])
#     else:
#         print('Error occurred:', response.status_code)

# # Ask user for location, price range, and ctegory
# user_location = input("Please enter your desired state: ")
# # user_price_range = input("Please enter your desired price range (e.g., $$, $$$): ")
# # user_category = input("Please enter your desired category (e.g., Italian, Mexican): ")

# # Call the function with user-provided preferences
# # get_restaurants(user_location, user_price_range, user_category)
# get_restaurants(user_location)

# # def main():
# #     print("Welcome to the Restaurant Finder Chatbot!")
# #     location = input("Please enter the city/state where you want to find restaurants: ")
# #     restaurants = get_restaurants(location)
    
# #     if restaurants:
# #         print("\nRestaurants in", location)
# #         for idx, restaurant in enumerate(restaurants, 1):
# #             print(f"{idx}. {restaurant['name']} - {restaurant['location']['address1']}")
# #     else:
# #         print("Error occurred while fetching restaurants. Please try again later.")

# # if __name__ == "__main__":
# #     main()