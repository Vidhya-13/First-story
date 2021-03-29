# -*- coding: utf-8 -*-
"""
Created on Mon Mar 29 13:33:23 2021

@author: nvidh
"""

import random
import string

total = string.ascii_letters + string.digits + string.punctuation

length = 16

password = "".join(random.sample(total, length))

print(password)
