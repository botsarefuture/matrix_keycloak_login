from settings import ELEMENT_URL, HOMESERVER_URL, USERNAME, PASSWORD, DEVICE_DISPLAY_NAME
import requests

SESSION = requests.Session()

def get_first():
    url = f"{HOMESERVER_URL}/_matrix/client/r0/login/sso/redirect/oidc?redirectUrl={ELEMENT_URL}/%23/"

    payload={}
    headers = {}

    response = SESSION.request("GET", url, headers=headers, data=payload, allow_redirects=False)
    return response

def get_second(location):
    url = location

    payload={}
    headers = {}

    response = SESSION.request("GET", url, headers=headers, data=payload, allow_redirects=False) 
    return response

def get_third(location):
    url = location

    payload=f'username={USERNAME}&password={PASSWORD}'
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = SESSION.request("POST", url, headers=headers, data=payload, allow_redirects=False)
    return response

def get_fourth(location):
    url = location

    payload={}
    headers = {}

    response = SESSION.request("GET", url, headers=headers, data=payload, allow_redirects=False)
    return response

def login(token):
    url = f"{HOMESERVER_URL}/_matrix/client/r0/login"

    payload = json.dumps({
    "type": "m.login.token",
    "token": token,
    "initial_device_display_name": DEVICE_DISPLAY_NAME
    })
    headers = {
    'authority': HOMESERVER_URL,
    'accept': 'application/json',
    'accept-language': 'fi-FI,fi;q=0.9,en;q=0.8',
    'content-type': 'application/json',
    'dnt': '1',
    'origin': ELEMENT_URL,
    'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    response = SESSION.request("POST", url, headers=headers, data=payload)
    return response