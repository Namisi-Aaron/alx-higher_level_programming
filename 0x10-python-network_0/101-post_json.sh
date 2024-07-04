#!/bin/bash
# This script ends a JSON POST request to a URL passed, and displays the body of the response
curl -s -X POST -H "Content-Type: application/json" -d @$2 $1
