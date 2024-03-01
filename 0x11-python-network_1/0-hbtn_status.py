#!/usr/bin/python3
"""
This script fetches the URL https://alx-intranet.hbtn.io/status using the urllib package.
The body of the response is displayed with a tabulation before each line.
"""

import urllib.request


def fetch_url():
    """
    Fetches the URL and prints the response body.
    """
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        lines = html.decode().split('\n')
        for line in lines:
            print('\t-', line)


if __name__ == "__main__":
    fetch_url()
