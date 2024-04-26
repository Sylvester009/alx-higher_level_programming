#!/bin/bash
# Make a request to the server with PUT method
curl -sLX PUT -d "user_id=yougotme" 0.0.0.0:5000/catch_me
