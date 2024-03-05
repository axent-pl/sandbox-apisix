import os
import requests

KC_ORIGIN = os.environ.get('KC_ORIGIN')
KC_CLIENT = os.environ.get('KC_CLIENT')
KC_SECRET = os.environ.get('KC_SECRET')
KC_USER = os.environ.get('KC_USER')
KC_PASS = os.environ.get('KC_PASS')

def get_token():
    url = f'{KC_ORIGIN}/auth/realms/bank/protocol/openid-connect/token'

    # Define the data payload
    payload = {
        'username': KC_USER,
        'password': KC_PASS,
        'grant_type': 'password',
        # 'grant_type': 'client_credentials',
        'client_id': KC_CLIENT,
        'client_secret': KC_SECRET
    }

    # Define the headers
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    # Make the POST request
    response = requests.post(url, data=payload, headers=headers)

    # Handle the response
    if response.status_code == 200:
        token_data = response.json()
        return "{} {}".format(token_data.get('token_type'), token_data.get('access_token'))
    else:
        print(response.json())
        raise Exception('Invalid token response')
    
if __name__ == '__main__':
    authorization = get_token()
    print(authorization)