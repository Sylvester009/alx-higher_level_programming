#!/usr/bin/python3
"""
takes in a URL and an email address,
sends a POST request to the passed URL
with the email as a parameter
"""
import sys
import requests


if __name__ == "__main__":
    email = {"email": sys.argv[2]}

    request = requests.post(sys.argv[1], data=email)
    print(request.text)
