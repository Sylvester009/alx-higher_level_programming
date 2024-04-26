#!/bin/bash
# Make a request to the server
curl -s -X POST "http://0.0.0.0:5000/catch_me" -d "user_id=yougotme"
