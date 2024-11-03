"""Write a program that fetches and prints out a random Chuck Norris joke for the user. Use the API presented here:
https://api.chucknorris.io/. The user should only be shown the joke text."""

import json
import requests

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request).json()
print(response["value"])

"""
try:
    response = requests.get(request).json()
    if response.status_code == 200:
        json_response = response.json()
        print(response["value"])
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")
"""