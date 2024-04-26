#!/usr/bin/python3
"""
takes in a URL, sends a request to the URL and displays the body of the response
"""
if __name__ == "__main__":
    import urllib.request
    from urllib.error import HTTPError
    import sys
  
    url = sysargv[1]
    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode("utf-8", "replace"))
    except HTTPError as e:
        print("Error code: {}".format(e.code)
