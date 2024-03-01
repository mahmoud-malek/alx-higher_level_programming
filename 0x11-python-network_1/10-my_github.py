#!/usr/bin/python3
"""a Python script that takes your GitHub credentials
 (username and password) and uses the GitHub API to display your id
"""

from requests.auth import HTTPBasicAuth
import sys
import requests


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    req = requests.get("https://api.github.com/user", auth=auth)
    print(req.json().get("id"))
