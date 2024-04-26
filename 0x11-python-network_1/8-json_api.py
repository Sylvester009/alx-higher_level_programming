#!/usr/bin/python3
"""
takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""
if __name__ == "__main__":
    import requests
    import sys
  
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    res = requests.post('http://0.0.0.0:5000/search_user', data={'q': letter})
    try:
        res_data = res.json()
        if res_data == {}:
            print('No result')
        else:
            print("[{}] {}".format(res_data.get('id'), res_data.get('name')))
    except ValueError:
        print('Not a valid JSON')
