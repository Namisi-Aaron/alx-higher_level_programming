#!/usr/bin/python3
"""This module defines a function lookup

lookup accepts an object and returns all
available attributes and methods of it"""
def lookup(obj):
    return dir(obj)
