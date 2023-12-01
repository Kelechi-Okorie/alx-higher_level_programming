#!/usr/bin/python3
"""sends a request using request package and displays
the variable X-Request-Id header variable"""

if __name__ == "__main__":
    import requests
    import sys

    url = sys.argv[1]
    r = requests.get(url)
    variable = r.headers.get('X-Request-Id')
    print(variable)
