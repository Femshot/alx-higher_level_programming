#!/usr/bin/python3
"""Displays the value of the X-Request-Id found in the header a URL"""
import urllib.request
from sys import argv


if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(response.headers['X-Request-Id'])
