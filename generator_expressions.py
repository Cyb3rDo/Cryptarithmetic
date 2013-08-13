#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Generator Expressions

# Experience with list comprehensions has shown their wide-spread utility
# throughout Python. However, many of the use cases do not need to have a
# full list created in memory. Instead, they only need to iterate over the
# elements one at a time.

# sum([x*x for x in range(10)])

# sum(x*x for x in range(10))

g = (x*x for x in range(10))

l = [x*x for x in range(10)]

print g
print l

for i in g:
	print i

for i in l:
	print i