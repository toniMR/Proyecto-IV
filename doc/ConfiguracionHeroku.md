#Explicación configuración Heroku

##Paso 1: Registrarse en Heroku
Primero hay que crearse una cuenta en [Heroku](https://www.heroku.com/)

##Paso 2: Crear una aplicación
Nos logueamos y creamos una aplicación. En mi caso el nombre que puse fue proyecciones-cine

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/heroku/creacion-appheroku.png)


##Paso 3: Archivos de configuración
Tenemos que crear un archivo Procfile en nuestro repositorio:
![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/heroku/Procfile.png)  

En el requeriments.txt añadimos gunicorn:  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/heroku/requirements.png)

##Paso 4: Asociar la cuenta de GitHub
- Vamos a nuestraAplicacion -> Deploy
- Deployment method: GitHub.
- App connected to Github: Ponemos nuestro repositorio
- Automatic deploys: Enable Automatic Deploys y marcamos Wait for CI to pass before deploy

##Paso 5: Desplegar la aplicación
De nuevo en Deploy nos vamos abajo del todo y le damos a Deploy Branch
Con esto ya debería de estar funcionando nuestro servicio.

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/heroku/desplegado.png)  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/heroku/desplegado-peliculas.png)
