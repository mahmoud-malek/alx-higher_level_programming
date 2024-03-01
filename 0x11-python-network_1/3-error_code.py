#!/usr/bin/python3
""" a Python script that takes in a URL,
 sends a request to the URL and displays the
  body of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys
    try:
        with request.urlopen(sys.argv[1]) as res:
            print(res.read().decode('UTF-8'))
    except error.HTTPError as error:
        print('Error code:', error.code)
