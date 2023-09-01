#!/usr/bin/python3
"""Script that fetches from a URL"""
import requests


if __name__ == "__main__":
    page = requests.get('https://intranet.hbtn.io/status')
    page_content = page.text
    print("Body response:")
    print(f"\t- type: {type(page_content)}")
    print(f"\t- content: {page_content}")
