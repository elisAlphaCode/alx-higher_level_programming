#!/usr/bin/python3
"""X-Request-Id variable found in the header of the response"""
import urllib.request
import sys


def fetcher():
    """fetcher"""
    with urllib.request.urlopen(sys.argv[1]) as response:
        header = response.info()
        print(header["X-Request-Id"])


if __name__ == "__main__":
    fetcher()
