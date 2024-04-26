#!/usr/bin/python3
"""
takes in a URL and an email, sends a POST request to the passed URL
"""
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    url = sys.argv[1]

    data = urllib.parse.urlencode({'email': sys.argv[2]})
    data = data.encode('utf-8')

    req = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
