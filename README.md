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

**Solicitudes que se pueden realizar al microservicios**
- Devolver todas las proyecciones de cada dia: https://proyecciones-cine.herokuapp.com/proyecciones

- Devolver todas las proyecciones que hay el dia 'd' https://proyecciones-cine.herokuapp.com/proyecciones/dia/7

- Devolver todas las proyecciones que hay el dia 'd' a partir de las 'hh:mm' https://proyecciones-cine.herokuapp.com/proyecciones/dia/12/hora/10:28

- Devolver todas las proyecciones que hay con peliculas que contengan 'n' en su nombre https://proyecciones-cine.herokuapp.com/proyecciones/pelicula/venom

- Devolver las proyecciones de una película para un día concreto https://proyecciones-cine.herokuapp.com/pelicula/venom/dia/9

### Docker

[Documentación-Docker](https://github.com/toniMR/Proyecto-IV/blob/master/doc/ConfiguracionDocker.md)  

Contenedor : https://contenedor-proyecciones.herokuapp.com/

Repositorio docker hub: https://hub.docker.com/r/tonimr/proyecto-iv/

[![Build Status](https://travis-ci.org/toniMR/Proyecto-IV.svg?branch=master)](https://travis-ci.org/toniMR/Proyecto-IV)
