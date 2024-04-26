#!/bin/bash
# Send request to URL and display status code
curl -s -I "$1" | grep -i "HTTP/" | awk '{print "Status code:", $2}'
