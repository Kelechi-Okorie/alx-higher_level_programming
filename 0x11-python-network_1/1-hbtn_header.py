#!/usr/bin/python3
"""Sends a request to a url and display the value
of the X-Request-Id variable found in the response header"""

if __name__ == "__main__":
    import urllib.request
    import sys

    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        variable = response.headers.get('X-Request-Id')
        print(variable)
