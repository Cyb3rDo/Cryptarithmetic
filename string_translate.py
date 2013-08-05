#!/usr/bin/env python
# -*- coding: utf-8 -*-

import string

enc_table = string.maketrans('ABCDEF', 'ZXTRSF')

dec_table = string.maketrans('ZXTRSF', 'ABCDEF')

enc = 'BED FACED'.translate(enc_table)

print enc

dec = enc.translate(dec_table)

print dec