#!/usr/bin/python3
"""This module contains the function safe_print_integer"""
def safe_print_integer(value):
    """this function prints an integer"""
    try:
        print('{:d}'.format(value))
        return True
    except Exception:
        return False
