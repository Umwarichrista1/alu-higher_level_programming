#!/usr/bin/python3
"""Module that displays the X-Request-Id header value for a given URL."""
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
