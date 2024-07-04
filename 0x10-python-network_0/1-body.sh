#!/bin/bash
# This script takes in a URL, sends a GET request to the URL, and displays the body of the response
STATUS_CODE=$(curl -s -L -o /dev/null $1 -w "%{http_code}\n")
if [ $STATUS_CODE -eq 200 ]; then
	curl -s -L $1
fi
