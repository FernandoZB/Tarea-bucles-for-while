# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:32:23 2023

@author: fzapber
"""

capital = float(input("Ingresa la cantidad a invertir: "))
interes_anual = float(input("Ingresa el interés anual en porcentaje: "))
num_anios = int(input("Ingresa el número de años: "))

for i in range(num_anios):
    capital *= 1 + (interes_anual / 100)
    print(f"Año {i+1}: {capital:.2f} €")
