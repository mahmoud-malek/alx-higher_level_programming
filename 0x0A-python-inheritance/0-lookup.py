#!/usr/bin/python3


""" A module """

def lookup(obj):
	""" a function """
	all = dir(obj)
	puplic = [attr for attr in all if not attr.startswith('__')]

	return puplic
