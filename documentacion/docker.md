## Como usar hub.docker.com ##

Deberemos realizar los siguientes pasos para desplegar nuestra aplicación en docker-hub:
- Registrarnos en [hub.docker.com](https://hub.docker.com/add/automated-build/github/orgs/?namespace=lorenmanu).
- Una vez registrados le daremos a **Create/Create Automated Build**.
- Despues indicaremos el repositorio que queremos sincronizar:
![img4](https://www.dropbox.com/s/f1qhv3f3kii5e74/img4.png?dl=1)
- Si se han realizado todos los pasos anteriores correctamente saldrá:
![img5](https://www.dropbox.com/s/48m4nnlza084whp/img5.png?dl=1)
- El Dockerfile que se usará para contruir la imagen se puede ver desde **hub.docker.com** aquí:
![img6](https://www.dropbox.com/s/9p89ewefjhcm4hw/img6.png?dl=1)

Para ejecutar la imagen en nuestra máquina anfitriona hay que realizar lo siguiente:

- Para descargar la imagen deberemos introducir en la terminal.
```
docker pull lorenmanu/submodulo-lorenzo

```

![img7](https://www.dropbox.com/s/yl4i0e5ft3lmpld/img7.png?dl=1)

- Para arrancar la imagen descargada en el paso anterior:

```
sudo docker run i -t lorenmanu/submodulo-lorenzo /bin/bash

```
![img8](https://www.dropbox.com/s/jdwqgser8f9ve5a/img8.png?dl=1)

- Nos vamos al directorio de la app, obtenemos su dirección ip con el comando **ifconfig**, y finalmente la lanzaremos pa visualizarla en nuestro ordenador:

![img9](https://www.dropbox.com/s/h9vb2a8jvsz83qg/xexo.png?dl=1)
