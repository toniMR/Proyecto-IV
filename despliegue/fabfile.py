# -*- coding: utf-8 -*-
from fabric.api import run, cd, sudo

# Descarga el proyecto e instala los requirements
def Install():
    run('git clone https://github.com/toniMR/Proyecto-IV.git')
    run('pip3 install -r requirements.txt')

# Lanza la aplicación
def Start():
    # Accede a la carpeta Proyecto-IV/src
    with cd("Proyecto-IV/src/"):
        sudo('gunicorn proyeccionesApp:app -b 0.0.0.0:80')
        print("Application started!")

# Para la aplicación
def Stop():
    sudo("pkill gunicorn")
    print("Application stoped!")

# Actualiza el proyecto
def Update():
    # Accede a la carpeta Proyecto-IV
    with cd("Proyecto-IV"):
        # Actualiza los archivos del proyecto
        sudo('git pull')
        # Instala los requirements
        run('pip3 install -r requirements.txt')
        print("Application updated!")

# Borra el proyecto
def Delete():
    sudo('rm -r Proyecto-IV')
