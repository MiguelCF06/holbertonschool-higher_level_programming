#!/usr/bin/python3
"""
takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""

import requests
import sys
url = "http://19f003bb820b.22216bed.hbtn-cod.io:5000/search_user"

if __name__ == "__main__":
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={"q": q})
    try:
        request_d = r.json()
        id = request_d.get("id")
        name = request_d.get("name")
        if not id or not name or len(request_d) == 0:
            print("No result")
        else:
            print("[{}] {}".format(request_d.get("id"), request_d.get("name")))
    except:
        print("Not a valid JSON")
