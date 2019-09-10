#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Calculadora:
    def __init__(self, a=0, b=0 ):
        self.__a = a
        self.__b = b

    def get_a(self):
        return self.__a

    def set_a(self, a):
        self.__a = a
    
    def get_b(self):
        return self.__b

    def set_b(self, b):
        self.__b = b

    def suma(self):
        return float(self.get_a() + self.get_b())

    def resta(self):
        return float(self.get_a() - self.get_b())

    def multi(self):
        return float(self.get_a() * self.get_b())

    def divi(self):
        return float(self.get_a() / self.get_b())  


conti = "0"

while conti == "0":
	seleccion = int(input("\nQue operación desea realizar:\n1.-SUMA.\n2.-RESTA.\n3.-PRODUCTO.\n4.-DIVISIÓN.\n"))

	operacion = {
	    1:"Suma",
	    2:"Resta",
	    3:"Multiplicacion",
	    4:"Division"
	}

	print("\nUd. selecciono la opción: ", operacion.get(seleccion))

	obj = Main()

	if seleccion == 1:
		a = float(input("\n\tIngresa el primer valor a "))
		b = float(input("\n\tIngresa el segundo valor b "))
		obj.set_a(a) 
		obj.set_b(b)	
		print("\nLa suma de a=", obj.get_a()," y b=",obj.get_b(), " es: ",obj.suma())
		conti = input("\nsi desea realizar otra operación presione 0 de lo contrario otra tecla para salir...\n") 	    
	elif seleccion == 2:
		a = float(input("\n\tIngresa el primer valor a "))
		b = float(input("\n\tIngresa el segundo valor b "))
		obj.set_a(a) 
		obj.set_b(b)	
		print("\nLa resta de a=", obj.get_a()," y b=",obj.get_b(), " es: ",obj.resta())
		conti = input("\nsi desea realizar otra operación presione 0 de lo contrario otra tecla para salir...\n") 	
	elif seleccion == 3:
		a = float(input("\n\tIngresa el primer valor a "))
		b = float(input("\n\tIngresa el segundo valor b "))
		obj.set_a(a) 
		obj.set_b(b)	
		print("\nLa Multiplicación de a=", obj.get_a()," y b=",obj.get_b(), " es: ",obj.multi())
		conti = input("\nsi desea realizar otra operación presione 0 de lo contrario otra tecla para salir...\n") 
	elif seleccion == 4:
		a = float(input("\n\tIngresa el primer valor a "))
		b = float(input("\n\tIngresa el segundo valor b "))
		obj.set_a(a) 
		obj.set_b(b)	
		print("\nLa división de a=", obj.get_a()," y b=",obj.get_b(), " es: ",obj.divi())
		conti = input("\nsi desea realizar otra operación presione 0 de lo contrario otra tecla para salir...\n")     
	else:
		print("\nSeleccione un valor valido comprendido entre 1 y 4")	
		conti = input("\nsi desea realizar otra operación presione 0 de lo contrario otra tecla para salir...\n") 	




