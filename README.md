# Proyecto-IV

## Microservicio de Proyección de Películas

El microservicio proporcionará información sobre las películas que hay en un cine. Mostrará las salas, horas y butacas disponibles.

### Explicación de las clases creadas por ahora
[Clases](https://tonimr.github.io/Proyecto-IV/doc/Clases)

### Explicación de las herramientas elegidas
[Herramientas](https://tonimr.github.io/Proyecto-IV/doc/Herramientas)

### Herramientas
- **Lenguaje:** Python
- **Framework:** Flask
- **Tests:** unitest y Travis CI
- **Base de datos:** MySQL

### PaaS
El PaaS que he escogido ha sido Heroku. Ya que en Azure se acaba el saldo y prefiero hacerlo primero con Heroku y aprender con Azure después.  

[Documentación-Heroku](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionHeroku.md)  

despliegue : https://proyecciones-cine.herokuapp.com/ 

También he puesto la ruta /peliculas (http://proyecciones-cine.herokuapp.com/peliculas) de modo que devuelve las películas que hay en el Cine. Pero si recargas empieza a añadirse de nuevo las películas en el JSON. Esto lo arreglaré cuando solucione una duda y suba las demás peticiones.  


### Docker

[Documentación-Docker](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionDocker.md)  



[![Build Status](https://travis-ci.org/toniMR/Proyecto-IV.svg?branch=master)](https://travis-ci.org/toniMR/Proyecto-IV)
