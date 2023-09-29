#!/usr/bin/python3
"""
Takes your GitHub credentials (username and personal access token)
and uses the GitHub API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    userToken = sys.argv[2]

    headers = {
        "Authorization": f"token {userToken}"
    }

    response = requests.get('https://api.github.com/user', headers=headers)

    if "json" not in response.headers.get('content-type'):
        print("Not a valid JSON")
    else:
        response = response.json()
        print(response.get('id'))
