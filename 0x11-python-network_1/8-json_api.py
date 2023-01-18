#!/usr/bin/python3
"""
script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""


import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        payload = {'q': sys.argv[1]}
    else:
        payload = {'q': ""}

    r = requests.post("http://0.0.0.0:5000/search_user", data=payload)

    try:
        r_json = r.json()
        if r_json == {}:
            print("No result")
        else:
            print("[{}] {}".format(r_json['id'], r_json['name']))
    except ValueError:
        print("Not a valid JSON")
