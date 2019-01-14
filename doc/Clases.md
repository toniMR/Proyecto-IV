# Explicación de los archivos de código fuente  


## Horas:

Se encarga de realizar todas las operaciones necesarias que tienen que ver con las horas. Como por ejemplo devolver la hora en la que termina una película pasando su hora de inicio y duración o si dos intervalos de tiempo se solapan.  


## Cine:

Esta clase es la encargada de gestionar todas las operaciones sobre
las películas y las proyecciones. Así como insertar películas o buscar proyecciones que proyecten una película, en un día y/o hora concretos.


## proyeccionesApp:

Se encargará de resolver todas las peticiones, devolviendo los JSON correspondientes. Diferenciará entre peticiones GET, POST, PUT, DELETE.  

Cada película está compuesta por los siguientes campos  

- id:        Identificador de la película  
- duracion:  Duracion de la película en formato "hh:mm"
- nombre:     Nombre de la película
- precio:     Precio por ver esa película  



Cada proyección esta compuesta por los siguientes campos:  

- id:        Identificador de la proyección (Se forma al insertar la -proyección)  
- dia:        Día de la proyección
- sala:       Numero de sala en la que se proyecta
- idPelicula  Identificador de la película que se proyecta


### Rutas

**/**    : (GET) Devuelve JSON {"status"="OK"}  

**/status** : (GET) Devuelve JSON {"status"="OK"}  


**'/peliculas'**:  

- (GET)  

Devuelve un JSON que es un array de diccionarios  

Cada diccionario es una película.  



- (POST)  

Acepta un JSON que puede ser un diccionario con los datos de una
película o un array de diccionarios. De manera que puede insertar
una película o varias según sea el JSON (array o diccionario)  


Devuelve un JSON con un diccionario con los siguientes campos:  

- 'mensaje' = "Películas insertadas -> (nº peliculas insertadas), Películas no insertadas -> (nº peliculas no insertadas))
- 'insertadas' = array con identificadores de las peliculas que se han insertado
- 'noInsertadas' = array con indentificadores de las peliculas que no se han insertado  


- (DELETE)  

Borra todas las películas de la BD y en consecuencia, todas las
proyecciones, ya que sin películas no se puede hacer ninguna
proyección.  


Devuelve un JSON con un diccionario con los siguientes campos:  

- "mensaje" = "Se han borrado todas las películas y proyecciones"
- "code" = "OK"


**'/peliculas/"id"'**:  

- (GET)  

Devuelve un JSON con los campos de la pelicula con identificador 'id'  


- (PUT)  

Acepta un JSON con el campo precio para modificar el precio a la pelicula con identificador 'id'  

Devuelve un JSON con:  

- Si existía la película con ese identificador  

"mensaje" = "Precio de la película cambiado"

- Si no existía la película con ese identificador  

"mensaje" = "No existe ningúna película con ese ID"  


- (DELETE)  

Borra la película identificada por 'id' y las proyecciones que la proyectaban  


Devuelve un JSON con:  

- Si existía la película con ese identificador  

"mensaje" = "Película y proyecciones borradas"  


- Si no existía la película con ese identificador  

"mensaje" = "No existe ningúna película con ese ID"  



**'/proyecciones'**:  

- (GET)  

Devuelve un JSON que es un diccionario que contiene diccionarios
La clave del diccionario es el dia (1 al 31) y el valor es un diccionario que tiene
como claves los identificadores de las proyecciones y su valor los datos de la proyección
presentados de la siguiente forma:  

id, dia, hora, sala y en vez de mostrar idPelicula contiene:  


pelicula: Diccionario con los datos de la pelicula(id, duracion, nombre, precio.)  

- (POST)  

Acepta un JSON que puede ser un diccionario con los datos de una
proyección o un array de diccionarios. De manera que puede insertar
una proyección o varias según sea el JSON (array o diccionario)  


Devuelve un JSON con un diccionario con los siguientes campos:  

- 'mensaje' = "Proyecciones insertadas -> (nº proyecciones insertadas), Proyecciones no insertadas -> (nº proyecciones no insertadas))
- 'insertadas' = array con identificadores de las proyecciones que se han insertado
- 'noInsertadas' = array con identificadores de las proyecciones que no se han insertado

- (DELETE)  

Borra todas las proyecciones de la BD.  


Devuelve un JSON con un diccionario con los siguientes campos:  

- "mensaje" = "Se han borrado todas las proyeciones correctamente"
- "code" = "OK"


**'/proyecciones/"id"'**:  

- (GET)  

Devuelve un JSON con los datos de la proyección con identificador 'id'  


- (PUT)  

Vi que estaba mal, poner algo si me da tiempo.  


- (DELETE)  

Borra la proyección identificada por 'id'.  


Devuelve un JSON con:  

- Si existía la película con ese identificador  

"mensaje" = "Proyección eliminada"  


- Si no existía la película con ese identificador  

"mensaje" = "No existe ningúna proyección con ese ID"  


**'/proyecciones/dia/"d"'**  

- (GET)  

Devuelve todas las proyecciones que hay el dia 'd'  



**'/proyecciones/dia/"d"/hora/"h"'**

- (GET)  

Devuelve todas las proyecciones que hay el dia 'd' a partir de las 'h'  

La hora se tiene que poner en formato hh:mm (Ej. 10:28)  



**'/proyecciones/pelicula/"n"'**  

- (GET)  

Devuelve todas las proyecciones que hay con peliculas que contengan 'n' en su nombre  


**'/proyecciones/pelicula/"n"/dia/"d"'**  

- (GET)  

Devuelve las proyecciones de una película para un día concreto  


**'/proyecciones/dia/"d"/sala/"s"'**  

- (GET)  

Devuelve las proyecciones de un día y sala concreta  


**'/importarDatosEjemplo'**  

- (GET)  

Borra todas las peliculas y proyecciones que hay e importa unas
película y proyecciones de Ejemplo  (contenidas en data/)  
