# Proyecto-IV
[![Build Status](https://travis-ci.org/toniMR/Proyecto-IV.svg?branch=master)](https://travis-ci.org/toniMR/Proyecto-IV)
[![License: GPL v3](https://img.shields.io/badge/License-GPL%20v3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://proyecciones-cine.herokuapp.com/)



## Microservicio de Proyección de Películas

El microservicio proporcionará información sobre las proyecciones que hay en un cine y las películas que proyecta. Se podrá consultar las películas que hay, los datos de una película determinada, las proyecciones disponibles, buscar proyecciones para un dia, hora y pelicula concretas. Además de modificarlas.

### Documentación del microservicio
[Clases](https://tonimr.github.io/Proyecto-IV/doc/Clases)  

### Herramientas
- **Lenguaje:** Python
- **Framework:** Flask
- **Tests:** unitest y Travis CI
- **Base de datos:** MongoDB en [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)  
- **PaaS:** Heroku  
- **IaaS:**  Azure  
- **Contenedor:** Docker  
- **Provisionamiento**  Ansible  
- **Despliegue**  Fabric  
- **Orquestador MV**  Vagrant


### Explicación de las herramientas elegidas
[Herramientas](https://tonimr.github.io/Proyecto-IV/doc/Herramientas)  

### PaaS
El PaaS que he escogido ha sido Heroku.

[Documentación-Heroku](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionHeroku.md)  

despliegue : https://proyecciones-cine.herokuapp.com/  

### Docker

[Documentación-Docker](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionDocker.md)  

Contenedor : https://contenedor-proyecciones.herokuapp.com/  

Repositorio docker hub: https://hub.docker.com/r/tonimr/proyecto-iv/


### Despliegue en Azure  

Despliegue del IasS en Azure haciendo uso de Fabric, Ansible y Vagrant.

[Documentación-DespliegueFinal](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionAzure.md)

Despliegue final: proyeccionescine.westus.cloudapp.azure.com  
