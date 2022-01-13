#!/usr/bin/python3
""" This module reads URL from server"""
import urllib.request as lib

with lib.urlopen('https://intranet.hbtn.io/status') as ericob:
    view = ericob.read()
print("Body response:")
print("\t- type: {}".format(type(view)))
print("\t- content {}".format(view))
print("\t- utf8 content: {}".format(view.decode()))
