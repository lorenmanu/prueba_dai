from django.db import models

class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	codigo = models.CharField(max_length=50)
	descripcion = models.TextField(max_length=200)
	foto = models.ImageField(upload_to='foto_producto')

	def __unicode__(self):
		return self.nombre