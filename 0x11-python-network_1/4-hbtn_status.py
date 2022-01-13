#!/usr/bin/python3
""" This script fetches url using requests package """
import requests

got = requests.get("https://intranet.hbtn.io/status")
print("Body response:")
print("\t- type: {}".format(type(got.text)))
print("\t- content: {}".format(got.text))

