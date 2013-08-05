#!/usr/bin/env python
# -*- coding: utf-8 -*-

userDefined = '23'

try:
    
    a = int(userDefined)
    
except ValueError:
    
    a = int(1)

except Exception:
    
    a = int(0)
    
finally:
    
    print a