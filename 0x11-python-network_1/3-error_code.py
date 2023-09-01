#!/usr/bin/python3
"""Sends a request to the URL and displays the body of the response
decoded in utf8 and handles error occured"""
import urllib.request
import urllib.error
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(argv[1]) as response:
            page = response.read()
            print(page.decode('utf8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
