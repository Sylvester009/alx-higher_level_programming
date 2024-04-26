#!/bin/bash
# Send request to URL and display status code
curl -sI -w '%{response_code}' "$1"
