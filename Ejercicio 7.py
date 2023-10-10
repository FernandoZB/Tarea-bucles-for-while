# -*- coding: utf-8 -*-
"""
Created on Tue Oct 10 10:37:34 2023

@author: fzapber
"""

contrasena_correcta = "contraseña"
contrasena = input("Ingresa la contraseña: ")
while contrasena != contrasena_correcta:
    print("Contraseña incorrecta. Intenta de nuevo.")
    contrasena = input("Ingresa la contraseña: ")
print("Contraseña correcta. Acceso concedido.")
