#!/usr/bin/python3
"""
takes your GitHub credentials
(username and password)
and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]

    res = requests.get("https://api.github.com/user", auth=(username, password))

    if res.status_code == 200:
        print(res.json()["id"])
    else:
        print(None)
