#This is the main file for IP location prg 

from data import get_IP_location
from ui import present

lat, lng = get_IP_location()
present(lat,lng)
