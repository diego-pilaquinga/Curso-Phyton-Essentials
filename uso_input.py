# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 17:12:38 2023

@author: DIEGO PILAQUINGA
"""

#Solicitud de los datos al usuario
nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
ubicacion = input("Ingrese su ubicación: ")
edad = input("Ingrese su edad: ")

#Concatenación de los datos ingresados
datos_usuario = "Mi nombre es " + nombre + " " + apellido + ", tengo " + str(edad) + " años y vivo en " + ubicacion + "."

#Impresión del párrafo con los datos ingresados
print(datos_usuario)