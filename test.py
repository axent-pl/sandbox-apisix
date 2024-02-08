import requests
import os
import re

KC_ORIGIN = 'http://localhost:2380'
KC_CLIENT = 'bank-app'
KC_SECRET = 'rifb7zJJzE2RKStq74pEPMg29W5GkyIC'
KC_USER = 'bank-app-user'
KC_PASS = 'bankappuserpass'

GW_ORIGIN = 'http://localhost:9080'
GW_SERVICE_HOST = 'grandioso-himalayan.gateway.bank'
GW_SERVICE_PATH = '/anything/of-foo'

MS1_ORIGIN = 'http://localhost:2280'
MS2_ORIGIN = 'http://localhost:3380'

def format_wrk_output(wrk_output, test_name):
    output = {
        'test_name': test_name
    }
    p_tc = r'^([0-9]+) threads and ([0-9]+) connections$'
    p_rps = r'^Requests\/sec:\s+(\d+\.\d*)'
    p_lat = r'^Latency\s+\d+'
    p_err = r'^Socket errors'

    for line in wrk_output.split('\n'):
        stripped_line = line.strip()

        m = re.match(p_tc, stripped_line)
        if m:
            output['threads'] = m[1]
            output['connections'] = m[2]
            continue

        m = re.match(p_rps, stripped_line)
        if m:
            output['requests_per_second'] = m[1]
            continue
        
        m = re.match(p_lat, stripped_line)
        if m:
            latency_data = stripped_line.split()[1:]
            output['latency'] = {
                'avg': latency_data[0],
                'stddev': latency_data[1],
                'max': latency_data[2]
            }
            continue

        m = re.match(p_err, stripped_line)
        if m:
            error_data = stripped_line.split(':')[1].split()
            output['errors'] = { error_data[idx]:error_data[idx+1] for idx in range(0,len(error_data),2) }
            continue
    
    return output

def get_token():
    url = f'{KC_ORIGIN}/auth/realms/bank/protocol/openid-connect/token'

    # Define the data payload
    payload = {
        'username': KC_USER,
        'password': KC_PASS,
        'grant_type': 'password',
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
        raise Exception('Invalid response')


def call_endpoint(authorization):
    url = f'{GW_ORIGIN}{GW_SERVICE_PATH}'
    headers = {
        'host': GW_SERVICE_HOST,
        'Authorization': authorization
    }
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print(response.status_code)
        print(response.text)
    else:
        raise Exception('Invalid response')

def run_wrk_tests():
    tests = []
    # cmd = f'ab -r -k -n 2000 -c 400 -H "Host: {GW_SERVICE_HOST}" -H "Authorization: {authorization}" {GW_ORIGIN}{GW_SERVICE_PATH}'
    for service,host in {'gateway':GW_ORIGIN}.items(): #'httpgobin':MS2_ORIGIN, 
        for connections in [10,20,50,100,200]:
            for threads in [1,2,3,4]:
                authorization = get_token()
                cmd = f'wrk -t{threads} -c{connections} -d30s -H "Host: {GW_SERVICE_HOST}" -H "Authorization: {authorization}" {host}{GW_SERVICE_PATH}'
                out = os.popen(cmd).read()
                test_name = f'{service}-t{threads}-c{connections}'
                tests.append(format_wrk_output(out, test_name))
                print(format_wrk_output(out, test_name))

    return tests

if __name__ == '__main__':
    authorization = get_token()
    call_endpoint(authorization=authorization)
    # run_wrk_tests()