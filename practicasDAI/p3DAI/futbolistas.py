# -*- coding: utf-8 -*-
__author__ = 'Lorenzo Manuel Rosas Rodríguez'

class Futbolista:

    def __init__(self, nombre, apellidos, correo, tarjeta,password,year,month,day):
        self.nombre = nombre
        self.apellidos = apellidos
        self.email = correo
        self.correo = correo
        self.tarjeta = tarjeta
        self.password = password
        self.year = year
        self.month = month
        self.day = day

    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "correo":self.correo,
            "tarjeta":self.tarjeta,
            "password":self.password,
            "year":self.year,
            "month":self.month,
            "day" : self.day
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - Edad: %i - Demarcación: %s - Internacional: %r" \
               %(self.nombre, self.apellidos, self.edad, self.password, self.password)
