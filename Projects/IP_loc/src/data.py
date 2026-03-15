#Prg to find aproxx location using IP address
import requests 

def get_IP_location():

    url = "http://ip-api.com/json/"

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        print("IP APT error", response.status_code)

    data = response.json()

    lat = data['lat']
    lng = data['lon']

    return lat, lng

