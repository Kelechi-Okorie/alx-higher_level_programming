#!/usr/bin/python3
"""Takes in a letter and sends a post request
with the letter as a parameter"""


if __name__ == "__main__":
    import requests
    import sys

    url = 'http://0.0.0.0:5000/search_user'
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    data = {"q": q}
    res = requests.post(url, data)
    try:
        result = res.json()
        if result == {}:
            print("No result")
        else:
            print("[{}] {}".format(result.get('id'), result.get('name')))
    except ValueError:
        print("Not a valid JSON")
