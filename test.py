import requests
import os

def get_token():
    url = 'http://localhost:2380/auth/realms/bank/protocol/openid-connect/token'

    # Define the data payload
    payload = {
        'username': 'banp-app-user',
        'password': 'bankappuserpass',
        'grant_type': 'password',
        'client_id': 'bank-app',
        'client_secret': 'rifb7zJJzE2RKStq74pEPMg29W5GkyIC'
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
        raise Exception('Invalid response')


def call_endpoint(authorization):
    url = 'http://localhost:9080/anything/of-foo'
    headers = {
        'host': 'grandioso-himalayan.gateway.bank',
        'Authorization': authorization
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.status_code)
        print(response.text)
    else:
        raise Exception('Invalid response')

def run_ab_tests(authorization):
    cmd = f'ab -r -n 2000 -c 200 -H "Host: grandioso-himalayan.gateway.bank" -H "Authorization: {authorization}" http://localhost:9080/anything/of-foo'
    out = os.popen(cmd).read()
    print(out)

if __name__ == '__main__':
    token = get_token()
    call_endpoint(authorization=token)
    run_ab_tests(authorization=token)
