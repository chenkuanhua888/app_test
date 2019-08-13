

import requests

if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/testapi/api-token-auth/'
    ret = requests.post(url, data={'username':'admin', 'password':'abc123abc'})
    print(ret.status_code)
    print(ret.text)
    token = ret.json()['token']
    print(token)
    #############################################
    url = 'http://127.0.0.1:8000/testapi/firstApi/'
    headers = {'Authorization': 'Token %s'%token}
    print(headers)
    ret = requests.get(url, headers=headers)
    print(ret.request.headers)
    print(ret.status_code)
    print(ret.text)