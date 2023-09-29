#!/usr/bin/python3
"""
This script sends a POST request to the provided URL with
an email parameter
and displays the body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    request = urllib.request.Request(url, data=data, method='POST')
    with urllib.request.urlopen(request) as response:
        content = response.read().decode('utf-8')
        print(content)
