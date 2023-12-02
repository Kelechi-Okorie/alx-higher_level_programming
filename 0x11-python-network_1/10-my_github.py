#!/usr/bin/python3
"""Uses GitHub credentials and GitHub API to display github id"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'https://api.github.com/user'
    username = sys.argv[1]
    password = sys.argv[2]
    res = requests.get(url, auth=(username, password))

    if res.status_code >= 400:
        print("None")
    else:
        data = res.json()
        print(data.get('id'))
