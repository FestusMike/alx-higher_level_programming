#!/usr/bin/python3
"""
This script fetches the status from https://alx-intranet.hbtn.io/status
using the requests package. It then displays information about
the response body.
"""
import requests

if __name__ == '__main__':
    url = 'https://alx-intranet.hbtn.io/status'

    content = requests.get(url)

    print("Body response:")
    print("\t- type:", type(content.text))
    print("\t- content:", content.text)
