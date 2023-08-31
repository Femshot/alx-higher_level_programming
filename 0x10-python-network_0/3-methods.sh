#!/bin/bash
# Display all HTTP methods a given server will accept
curl -Is "$1" | grep Allow | cut -c 8-
