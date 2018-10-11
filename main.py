import base64
import jwt
import time
import requests
import getpass
import json
import sys

username = input("username> ")
password = getpass.getpass("password> ")

url = "http://localhost:12345" + "/user/auth"

try:
    resp = requests.get(
        url, headers={"username": username, "password": password})
    if resp.status_code >= 300:
        raise IOError("Login failed [" + str(resp.status_code) +
                      "]: " + json.loads(resp.content)['message'])
    else:
        auth_token = resp.content
except Exception as e:
    print("Connection to AUTH couldn\'t be established\n", e)
    sys.exit(-1)

for _ in range(10):
    url = "http://localhost:9876" + "/numbers"
    try:
        resp = requests.get(
            url, headers={"authorization": auth_token})
        if resp.status_code >= 300:
            raise IOError("Lucky Numbers recovery failed [" + str(resp.status_code) +
                          "]: " + json.loads(resp.content)['message'])
    except Exception as e:
        print("Connection to LUCKYNUMBERS couldn\'t be established\n", e)
        sys.exit(-1)
    print(json.loads(resp.content)['numbers'])
    time.sleep(2)
