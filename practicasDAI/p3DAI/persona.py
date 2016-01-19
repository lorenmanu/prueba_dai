# -*- coding: utf-8 -*-
__author__ = 'Lorenzo Manuel Rosas Rodríguez'

class Persona:

    def __init__(self, nombre, apellidos, VISA, correo, birthday,birthmoth,birthyear,password):
        self.nombre = nombre
        self.apellidos = apellidos
        self.correo = correo
        self.VISA=VISA
        self.birthday=birthday
        self.birthmoth=birthmoth
        self.birthyear=birthyear
        self.password=password

    def toDBCollection (self):
        return {
            "nombre":self.nombre,
            "apellidos":self.apellidos,
            "correo":self.correo,
            "VISA":self.VISA,
            "dia":self.birthday,
            "mes":self.birthmoth,
            "year":self.birthyear,
            "password":self.password
        }

    def __str__(self):
        return "Nombre: %s - Apellidos: %s - correo: %i - VISA: %s - DIA: %r" \
               %(self.nombre, self.apellidos, self.correo, self.VISA, self.birthday)
