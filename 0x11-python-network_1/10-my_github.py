#!/usr/bin/python3
"""
takes your Github credentials (username and password) and uses the Github API
to display your id
"""

import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    r = requests.get("https://api.github.com/users/{}".format(sys.argv[1]),
                     auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    print(r.json().get("id"))
