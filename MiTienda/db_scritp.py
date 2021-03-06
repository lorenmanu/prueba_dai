import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MiTienda.settings.py')

import django
django.setup()

from apps.tiendas.models import Zona, Tienda


def populate():
    zona_aux = add_zona(nombre='Granada',localizacion='Granada')

    add_tienda(nombre='Corseteria Europa',
        calle="Sagrada Familia",
        zona=zona_aux,
        imagen='/Users/lorenzo/Desktop/prueba_dai/media/tmp/tienda_prueba.png')

    # Print out what we have added to the user.
    for z in Zona.objects.all():
        for t in Tienda.objects.filter(zona=z):
            print "- {0} - {1}".format(str(c), str(p))

def add_zona(nombre, localizacion, views=0):
    zona = Zona.objects.get_or_create(nombre=nombre, localizacion=localizacion,views=views)[0]
    zona.save()
    return p

def add_tienda(nombre,calle,zona,imagen,views=0):
    tienda = Tienda.objects.get_or_create(nombre=nombre,calle=calle,zona=zona,imagen=imagen,views=views)[0]
    return c

if __name__ == '__main__':
    print "Empezando a llenar la base de datos"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')
    from apps.tiendas.models import Tienda, Zona
    populate()