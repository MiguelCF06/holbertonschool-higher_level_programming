#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response
"""
import urllib.request
import sys
import urllib.error

if __name__ == "__main__":
    req = urllib.request.Request(sys.argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
