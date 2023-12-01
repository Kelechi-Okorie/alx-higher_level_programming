#!/usr/bin/python3
"""Sends a request to a url, displays the content and
manages the error in case of excetion"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError, HTTPError
    import sys

    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            res = response.read()
            print(res.decode('utf-8', 'replace'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
