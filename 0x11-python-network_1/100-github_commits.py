#!/usr/bin/python3
"""lists 10 commits from repo rails by the user rails"""


if __name__ == "__main__":
    import requests
    import sys

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    res = requests.get(url)
    if res.status_code >= 400:
        print("None")
    else:
        for commit in res.json()[0:10]:
            sha = commit.get("sha")
            name = commit.get("commit").get("author").get("name")
            print("{}: {}".format(sha, name))
