#!/usr/bin/python3
"""
Takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {'q': q}
    response = requests.post(url, data=data)

    # Check if the response content-type is JSON
    if response.headers.get('content-type') == 'application/json':
        json_response = response.json()
        # Check if the JSON response is not empty
        if json_response:
            print("[{}] {}".format(json_response['id'], json_response['name']))
        else:
            print("No result")
    else:
        print("Not a valid JSON")
