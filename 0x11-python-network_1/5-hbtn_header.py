#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and
displays the value of the variable X-Request-Id
"""
import sys
import requests


if __name__ == "__main__":
    res = requests.get(sys.argv[1])
    request_id = res.headers.get('X-Request-Id')

    print(request_id)
