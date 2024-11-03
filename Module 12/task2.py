"""Familiarize yourself with the OpenWeather weather API at: https://openweathermap.org/api. Your task is to write a
program that asks the user for the name of a municipality and then prints out the corresponding weather condition
description text and temperature in Celsius degrees. Take a good look at the API documentation. You must register for
the service to receive the API key required for making API requests. Furthermore, find out how you can convert Kelvin
degrees into Celsius."""

import json
import requests

municipality: str = input("Enter a municipality: ")

request = f"https://api.openweathermap.org/data/2.5/weather?q={municipality}&appid=1e386c6e1a88d3a3a42a4bea92dc7325&units=metric"

response = requests.get(request).json()

print(response["main"]["temp"], end = "")
print(" Degrees Celsius")
print(response["weather"][0]["description"])