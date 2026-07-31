#!/usr/bin/python3
"""Module that searches for a user via the search_user API endpoint."""
import requests
import sys


if __name__ == "__main__":
    letter = ""
    if len(sys.argv) > 1:
        letter = sys.argv[1]
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={'q': letter})
    try:
        json_data = response.json()
        if json_data:
            print("[{}] {}".format(json_data.get('id'), json_data.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
