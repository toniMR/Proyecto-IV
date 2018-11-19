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
