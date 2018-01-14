# -*- coding: utf-8 -*-
"""
Created on Thu Dec 28 15:57:38 2017

@author: Dell
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = [z1 for z1 in a for z2 in b if(z1 == z2)]

d = []

e = [d.append(i) for i in c if i not in d]

print(d) 