#!/bin/bash
# Takes in a URL, sends a request, and displays the size of the body of the response
curl -sI "$1" | awk '/Content-Length/ {print $2}'
