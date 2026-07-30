#!/bin/bash
# displays all HTTP methods a server accepts for the given URL
curl -si -X OPTIONS "$1" | grep -i "^allow:" | cut -d " " -f2- | tr -d "\r"
