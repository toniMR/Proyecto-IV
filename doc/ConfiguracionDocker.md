# Explicación configuración Docker

## Paso 1: Registrarse en Docker hub
Primero hay que crearse una cuenta en [Docker hub](https://hub.docker.com/)


Una vez registrado, nos vamos a settings -> Linked Accounts & Services, pinchamos sobre github y aceptamos la autorización.  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/docker/linkedgithub.png)

Después nos vamos a Create -> Create Automated Build y enlazamos nuestro proyecto.


## Paso 2: Instalar Docker
[Documentación Docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)

Actuualizamos los paquetes

	$ sudo apt-get update

Instalamos los paquetes necesarios 

	$ sudo apt-get install \
	    apt-transport-https \
	    ca-certificates \
	    curl \
	    software-properties-common

Añadimos la key GPG oficial de Docker

	$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

Verificamos la clave

	$ sudo apt-key fingerprint 0EBFCD88

Establecemos un repositorio estable

	$ sudo add-apt-repository \
	   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
	   $(lsb_release -cs) \
	   stable"

Actualizamos paquetes e instalamos la última versión de Docker

	$ sudo apt-get update
	$ sudo apt-get install docker-ce

Verificamos si se ha instalado correctamente.

	$ sudo docker run hello-world

## Paso 3: Crear Dockerfile

En el Dockerfile pondremos las ordenes que necesitamos para crear la imagen:


FROM python:3

# Datos del creador
MAINTAINER toni97sk8@gmail.com

# Establecer directorio 
WORKDIR src/

# Copiar contenido
COPY . .

# Instalar requerimientos encesarios
RUN pip install --no-cache-dir -r requirements.txt

# Asignamos el puerto 80 al contenedor
EXPOSE 80

# Lanzamos la aplicación
CMD cd src && proyeccionesApp:app 


## Paso 4: Desplegar en Heroku
[Documentación Heroku.yml](https://devcenter.heroku.com/articles/build-docker-images-heroku-yml)

Creamos una aplicación nueva en heroku, a la que llamare contenedor-proyecciones

Creamos el archivo heroku.yml para que cree la imagen desde el dockerfile.

	build:
	  docker:
	    web: Dockerfile
	run:
	  web: cd src && gunicorn proyeccionesApp:app

Indicamos en Heroku que tenemos un contenedor con:
	heroku stack:set container -a contenedor-proyecciones

Actualizamos:
	git push heroku master

(A mi me daba un error y lo arreglé con lo siguiente):
	heroku git:remote -a contenedor-proyecciones

Y de nuevo:
	git push heroku master



















