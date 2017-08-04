#!/usr/bin/env python
import pwd
import sys

def user(username, shell=None):
    """Check if user exists"""
    try:
        pwd.getpwnam(username)
        print("User ok")
    except KeyError:
        print('User {} does not exist.'.format(username))

username = sys.argv[1]

user(username)