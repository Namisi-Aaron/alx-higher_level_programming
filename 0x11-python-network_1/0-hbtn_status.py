#!/usr/bin/python3
"""This script fetches https://alx-intranet.hbtn.io/status"""
if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        utf_body = body.decode('utf-8')

        print(type(body))
        output = (
              'Body response:\n'
              f'    - type: {type(body)}\n'
              f'    - content: {body}\n'
              f'    - utf8 content: {utf_body}'
              )
        print(output)
