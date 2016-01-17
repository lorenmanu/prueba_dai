###Despliegue remoto Fabric

Para realizarlo tendremos que tener creada una instancia en ec2, la explicación de su creación se detalla en **ec2.md** en la carpeta documentación del proyecto. Los pasos realizados para el despliegue son:

**Primero**: Localizar nuestro archivo con la clave privada proporcionada por Amazon. Este archivo tendrá extensión **.pem** y Amazon nos permitirá su descarga cuando creemos la instancia(**documentacion/ec2.md**). Copiaremos la ruta a dicho archivo y lo añadiremos a la conexíon **ssh** con el siguiente comando:

```
ssh-add "ruta archivo"

``
En el siguiente pantallazo muestro como Amazon me indica realizar la conexión ssh, con el correspondiente archivo(**extensión .pem**), como lo busco y lo añado a ssh.

![img1](https://www.dropbox.com/s/exnxucut9noig86/img1_iv.png?dl=1)

**Nota**: antes de añadir el archivo a ssh debemos ponerle los permisos adecuados, por lo que en la terminal indicaremos:

```
chmod 400 "nombre_archivo".pem

```

**Segundo**: Una vez realizado el paso anterior, me dispongo a usar mi archivo **fabfile.py**. En este archivo tengo diferentes tareas automatizadas para realizarlas por ssh. Para ello, tendremos que dirigirnos al directorio donde se encuentra el archivo **fabfile.py** y seguir la siguiente sintaxis en la terminal:

```
fab -H NombreUsuario@Nombredelhost/o/IPelhost operación

```

Las operaciones que permite realizar mi **fabfile.py** son:

- Obtener información del host:
![img2](https://www.dropbox.com/s/lvkbxodkdqcmj3k/img2_iv.png?dl=1)

- Descargar la aplicación:
![img3](https://www.dropbox.com/s/67dmce3q2tah8hc/img3_iv.png?dl=1)

- Instalar las dependencias:
![img4](https://www.dropbox.com/s/glgtkxdd20tomyh/img4_iv.png?dl=1)

- Sincronizar la base de datos:
![img5](https://www.dropbox.com/s/atad1g9cs1taf5p/img5_iv.png?dl=1)

- Realizar los tests en local:
![img6](https://www.dropbox.com/s/loi6aznjpgmdlrl/img6_iv.png?dl=1)

- Ejecución de la aplicación:
![img7](https://www.dropbox.com/s/insyi6vmy5vsuzj/img7_iv.png?dl=1)

**Nota**: como se puede ver en la anterior imagen se ha ejecutado la aplicación y accedido a ella por el navegador desde el DNS que nos da Amazon(**documentacion/ec2.md**). Esto es posible si configuramos las reglas correctamente, se detallará en **documentacion/ec2.md**.

El enlace de mi app en ec2 de Amazon se puede ver [aquí](ec2-52-11-219-71.us-west-2.compute.amazonaws.com).

###Despliegue con docker.
Si queremos realizar el despliegue usando el docker, bastará con usar las operaciones del archivo **fabfile.py** para ese propósito:

- Descarga del docker:
![img8](https://www.dropbox.com/s/0mqlavcpcgi3ux6/img8_iv.png?dl=0)
- Ejecutar docker:
![img9](https://www.dropbox.com/s/wab4995g1vzk5k5/img9_iv.png?dl=1)







