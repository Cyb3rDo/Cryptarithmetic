#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Function explanation:
# - solve --> Runs through all possible combinations testing each for valid
# - fill_in --> Create a new formula replacing letters with numbers
# - valid --> Tests our filled-in string

import re

def valid(formula):
	"""
	Formula is valid only if has no leading zero on any of it's numbers
	and the formula evaluates as True.
	Returns True or False
	"""
	try:
		return not re.search(r'\b0[0-9]', formula) and eval(formula) is True
	except ArithmeticError:
		return False
	except:
		return False

print valid('1+1==2')
