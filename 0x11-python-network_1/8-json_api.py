#!/usr/bin/python3
""" Searches and API and sends a Post """
import requests
from sys import argv


if __name__ == "__main__":

    if len(argv) < 2:
        pay = {'q': ""}
    else:
        pay = {'q': argv[1]}

    req = requests.post('http://0.0.0.0:5000/search_user', data=pay)
    if req.status_code == requests.codes.ok:
        try:
            code = req.json()
            if code == {}:
                print("No result")
            else:
                print(f'[{code["id"]}] {code["name"]}')
        except Exception:
            print("Not a valid JSON")
