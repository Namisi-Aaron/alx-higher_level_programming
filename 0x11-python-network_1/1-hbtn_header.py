#!/usr/bin/python3
"""
This script takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request
    from sys import argv
    url = argv[1]
    with urllib.request.urlopen(url) as response:
        headers = dict(response.getheaders())
        value = headers.get('X-Request-Id')
        print(value)
