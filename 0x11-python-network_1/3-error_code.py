#!/usr/bin/python3
"""
script that takes in a URL, sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""


import sys
from urllib import request, error
if __name__ == "__main__":
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as resp:
            html = resp.read()
            print("{}".format(html.decode('utf-8')))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
