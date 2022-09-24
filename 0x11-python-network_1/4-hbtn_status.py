#!/usr/bin/python3
"""Write a Python script that fetches https://alx-intranet.hbtn.io/status"""
import requests


def status():
    """status"""
    r = requests.get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))


if __name__ == "__main__":
    status()
