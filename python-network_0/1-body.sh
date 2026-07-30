#!/bin/bash
# sends a GET request and displays the body only if status code is 200
[ "$(curl -s -o /dev/null -w "%{http_code}" "$1")" -eq 200 ] && curl -s "$1"
