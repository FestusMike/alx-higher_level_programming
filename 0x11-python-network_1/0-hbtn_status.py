#!/usr/bin/python3
"""
A script that fetches https://alx-intranet.hbtn.io/status
using the urllib package.
"""
import urllib.request

if __name__ == '__main__':

    # Open the URL and fetch its content
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        content = response.read()

        # Display information about the response
        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
