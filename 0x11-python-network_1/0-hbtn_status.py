#!/usr/bin/python3
"""
Script to fetch and display https://alx-intranet.hbtn.io/status
using urllib package.
"""

if __name__ == '__main__':
    import urllib.request as req

    with req.urlopen('https://alx-intranet.hbtn.io/status') as res:
        content = res.read()
        decoded_content = content.decode('utf-8')

        print("Body response:")
        print("\t- type: {}".format(type(content)))
        print("\t- content: {}".format(content))
        print("\t- utf8 content: {}".format(content.decode('utf-8')))
