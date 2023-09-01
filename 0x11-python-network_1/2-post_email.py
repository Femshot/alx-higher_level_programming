#!/usr/bin/python3
"""Sends POST request for email variabe to a URL"""
import urllib.request
import urllib.parse
from sys import argv


if __name__ == "__main__":
    data = {}
    data["email"] = argv[2]
    mail = urllib.parse.urlencode(data)
    mail = mail.encode('ascii')
    req = urllib.request.Request(argv[1], mail)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode("utf8"))
