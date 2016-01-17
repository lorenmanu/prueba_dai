### Creación de la instancia ec2

Una vez registrados en Amazon, donde tendremos que dar una tarjeta de crédito y seguir una serie de trámites(son muy estrictos para mi gusto), se procede a crear una instancia, para ello se siguen los siguientes pasos:

- Nos dirigimos al apartado **EC2 VIRTUAL SERVERS IN THE CLOUD**.

![img10](https://www.dropbox.com/s/2bfpzbkdlo2ygyx/img10_iv.png?dl=0)

- Una vez dentro nos vamos al apartado **Instances**.

![img11](https://www.dropbox.com/s/fhmkr9dfmot239l/img11_iv.png?dl=1)

- Le damos a la pestaña **Launch Instance**.

![img12](https://www.dropbox.com/s/luntkxme7qtzxgi/img12_iv.png?dl=1)

**Nota**: Una vez aquí nos pedirán el sistema operativo que queramos, características..., me los saltaré porque no son muy relevantes para el proceso, quiero detallarme más en lo siguiente que es importante. Lo importante de este paso es que nos dirán que nos descarguemos un archivo en extensión **.pem**, que será el que contrendrá la clave secreta y el que nos permitirá realizar la conexión a nuestra instancia por ssh.

- Una vez creada la máquina, tendremos que indicar las peticiones que queremos atender, para ello nos tenemos que fijar en la pestaña **description** en el apartado **Security groups** el nombre que tiene, en mi caso es **launch-wizard-3**. En el apartado **description** también podemos ver otra información, como puede ser la ip pública, el dns que nos da Amazon...

![img14](https://www.dropbox.com/s/d5jgusar1pe9mw2/img14_iv.png?dl=1)

- Nos dirigimos al apartado **Security groups**, seleccionando el nombre que está sombreado en azul de la anterior imagen y le damos a la pestaña **Inbound**, como se pude observar hay una serie de reglas que podemos editar para eliminarlas o añadir más.

![img15](https://www.dropbox.com/s/d95pnycmw0fuqky/img15_iv.png?dl=1)

![img16](https://www.dropbox.com/s/2190m8k8ks0ao8w/img16_iv.png?dl=1)
**Nota**: Como se puede ver en la última imagen mi máquina esta configurada para antender peticiones que le llegan tanto por tcp como por ssh.