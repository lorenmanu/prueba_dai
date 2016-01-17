from django.views.generic import CreateView,TemplateView,ListView
from .models import Producto
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
import datetime
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from serializers import productoSerializar

class Registrarproducto(CreateView):
	template_name = 'productos/registrarproducto.html'
	model = Producto
	success_url = reverse_lazy('reportar_producto')

	

class Reportarproducto(ListView):
	template_name = 'productos/reportarproducto.html'
	model = Producto
	context_object_name = 'productos'

class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def productos_lista(request):
	"""
	Lista todos los nombres de personas o la crea
	"""
	if request.method == 'GET':
		productos = Producto.objects.all()
		serializador = productoSerializar(productos, many=True)
		return JSONResponse(serializador.data)
	
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = productoSerializar(data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data, status=201)
		return JSONResponse(serializador.errors, status=400)

@csrf_exempt
def producto_detalle(request, pk):
	"""
	Recuperar, actualizar o borrar una persona
	"""
	try:
		producto = Producto.objects.get(pk=pk)
	except producto.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializador = productoSerializar(producto)
		return JSONResponse(serializador.data)
	#elif request.method == 'PUT':
	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializador = puestionSerializar(producto, data=data)
		if serializador.is_valid():
			serializador.save()
			return JSONResponse(serializador.data,status=202)
		return JSONResponse(serializador.errors, status=400)
	elif request.method == 'DELETE':
		producto.delete()
		return HttpResponse(status=204)