# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:30:56 2023

@author: fzapber
"""

n = int(input("Introduce un número entero positivo: "))
for i in range(n, -1, -1):
    print(i, end=", ")