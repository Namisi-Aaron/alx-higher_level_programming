#!/usr/bin/python3
"""
This script takes in a URL,
sends a request to the URL
and displays the value of the X-Request-Id variable
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    from sys import argv
    url = argv[1]
    email = argv[2]
    data = {'email': email}
    encoded_data = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url, data=encoded_data)
    with urllib.request.urlopen(request) as response:
        output = response.read().decode('utf-8')
        print(output)
