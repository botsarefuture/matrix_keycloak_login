import requests
import json
from requesting import get_first, get_second, get_third, get_fourth

try: 
    from BeautifulSoup import BeautifulSoup
except ImportError:
    from bs4 import BeautifulSoup

response = get_first()
response = get_second(response.headers["Location"])
response = get_third(BeautifulSoup(response.text, features="lxml").body.find('form')["action"])
response = get_fourth(response.headers["Location"])
token = response.headers["Location"].split("loginToken=")[1].replace("#/", "")

login_data = login(TOKEN).json()

access_token = login_data["access_token"]

print(access_token)