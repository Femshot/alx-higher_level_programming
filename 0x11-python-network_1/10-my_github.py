#!/usr/bin/python3
import requests as rq
from sys import argv

token = f"Bearer {argv[2]}"
heads ={"Accept": "application/vnd.github+json",
        "Authorization": token,
        "X-GitHub-Api-Version": "2022-11-28"}
url = "https://api.github.com/user"

response = rq.get(url, headers=heads)
print(response.json()['id'])
