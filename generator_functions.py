#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generator Functions

# Generators are a simple and powerful tool for creating iterators.
# They are written like regular functions but use the yield statement
# whenever they want to return data

def count(start, end = None):
	i = start
	yield i
	while i <= end or end == None:
		yield i
		yield -i
		i = i+1

c = count(0)
print c

for i in range(100):
	print c.next()