import json
import requests


KC_ORIGIN = 'http://localhost:2380'
KC_CLIENT = 'bank-app'
KC_SECRET = 'rifb7zJJzE2RKStq74pEPMg29W5GkyIC'
KC_USER = 'bank-app-user'
KC_PASS = 'bankappuserpass'

GW_A6SA_ORIGIN = 'http://localhost:9081'
GW_A6DC_ORIGIN = 'http://localhost:9080'

GW_SERVICE_HOST = 'adagio-angora.gateway.bank'
GW_SERVICE_PATH = '/anything/of-foo'

MS_ORIGIN = 'http://localhost:3380'

SERVICES = {
    'apisix': GW_A6SA_ORIGIN,
    'apisix-decoupled': GW_A6DC_ORIGIN,
    # 'kong': GW2_ORIGIN,
    'go-httpbin': MS_ORIGIN
}


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


def call_endpoint(endpoint,authorization):
    url = f'{endpoint}{GW_SERVICE_PATH}'
    headers = {
        'host': GW_SERVICE_HOST,
        'Authorization': authorization
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('Invalid gateway response')


if __name__ == '__main__':
    authorization = get_token()
    # print(authorization)
    # exit(0)
    reqs = []
    for service, url in SERVICES.items():
        try:
            resp = call_endpoint(endpoint=url, authorization=authorization)
        except:
            print(f'service {service} failed')
            exit(1)
        reqs.append({
            'id': service,
            'url': f'{url}{GW_SERVICE_PATH}',
            'method': 'GET',
            'headers': {
                'Authorization': authorization,
                'host': GW_SERVICE_HOST
            }
        })
    print(json.dumps(reqs))