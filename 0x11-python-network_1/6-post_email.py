#!/usr/bin/python3
"""Sends a POST request to the passed URL with an email as a parameter"""
import requests
from sys import argv


if __name__ == "__main__":
    to_post = {'email': argv[2]}
    page = requests.post(argv[1], to_post)
    print(page.text)
