# my_map_app_calculate_distance.py
import requests
import os

def get_distance(origin, destination):
    api_key = os.getenv("GOOGLE_API_KEY")
    url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    params = {
        "origins": origin,
        "destinations": destination,
        "key": api_key
    }

    response = requests.get(url, params=params)
    data = response.json()

    if data["status"] != "OK":
        raise Exception(f"API Error: {data['status']}")

    element = data["rows"][0]["elements"][0]
    if element["status"] != "OK":
        raise Exception(f"Element Error: {element['status']}")

    return element["distance"]["text"]
