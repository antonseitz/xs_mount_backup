#!/bin/python

def banner(text):
    red()
    print( (" " + text + " ").center(60,"#"))
    white()

def red():
    print("\033[31m")

def white():
    print("\033[0m")

def ask(text):
    return raw_input(text + " [ENTER to confirm / other key to skip ] ? ")


def ask_text(text):
    return raw_input(text )