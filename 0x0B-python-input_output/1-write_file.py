#!/usr/bin/python3
"""Module that writes a string to a text file"""


def write_file(filename="", text=""):
    """writes a string to a text file
    Return: number of characters written"""
    with open(filename, encoding="utf-8", mode="w+") as f:
        return f.write(text)
