from django.contrib import admin
from .models import Tienda,Zona, UserProfile


# Register your models here.

admin.site.register(Tienda)
admin.site.register(Zona)
admin.site.register(UserProfile)