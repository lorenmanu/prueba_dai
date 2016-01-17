from django.conf.urls import patterns, include, url
from apps.productos.views import Registrarproducto,Reportarproducto


urlpatterns = patterns('', 
    url(r'^registrar/$' , Registrarproducto.as_view() , name="registrar_producto"),
    url(r'^reportar/$' , Reportarproducto.as_view() , name="reportar_producto"),
	url(r'^productoslist/$', 'apps.productos.views.productos_lista'),
    url(r'^productodetail/(?P<pk>[0-9]+)/$', 'apps.productos.views.producto_detalle'),

)
