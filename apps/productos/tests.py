"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import datetime

from django.utils import timezone
from django.test import TestCase

from models import Producto

# Create your tests here.
from rest_framework import status
from rest_framework.test import APITestCase

class RutasTests(APITestCase):

    def producto(self):
        q1 = Producto(nombre='Armario',codigo='1234',descripcion='Hola',foto='http://localhost:8000/media/foto_producto/220px-Cervantes_Valladolid_lou.jpg')
        q1.save()
        self.assertEqual(response.content,'{"nombre":"Cervantes","codigo":"1234","descripcion":"Hola","foto":"http://localhost:8000/media/foto_producto/220px-Cervantes_Valladolid_lou.jpg"}')
        print("Question consultada XD1")

    def test_detalle_varios_productos(self):
        q1 = Producto(nombre='Armario' , codigo='1234',descripcion='Hola',foto='foto1')
        q1.save()
        q2 = Producto(nombre='Armario(2)' , codigo='1234(2)',descripcion='Hola(2)',foto='foto2')
        q2.save()
        response = self.client.get('/producto/productoslist/')
        self.assertEqual(response.content,'[{"nombre":"Armario","codigo":"1234","descripcion":"Hola","foto":"http://localhost:8000/media/foto1"},{"nombre":"Armario(2)","codigo":"1234(2)","descripcion":"Hola(2)","foto":"http://localhost:8000/media/foto2"}]')
        print("Varias personas consultadas en detalle correctamente2")



