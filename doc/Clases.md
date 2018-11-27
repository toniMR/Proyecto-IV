# Explicación de las clases creadas

**Cine:** Esta clase es la encargada de inicializar todas las proyecciones de cada día y de gestionar las solicitudes como buscar proyecciones de una pelicula, dia o hora concretos.

**proyeccionesApp:** Se encargará de resolver todas las peticiones, devolviendo los json correspondientes.  


Anteriormente, tenía también las siguientes clases:

**Película:** Esta clase almacena información sobre la película como el nombre y la duración

**Proyección:** Esta clase almacena información sobre la proyección como el dia, hora, sala en la que se proyecta y la película que se proyecta.

Pero como no tenían métodos que difieran de devolver sus atributos las he quitado de momento. Si añado más funcionalidades podría ir creando esos objetos en cuanto cargo el .json y así luego usar sus métodos de una forma más limpia.
