from fabric.api import *

def Start():
    with cd("Proyecto-IV/src"):
        sudo('gunicorn proyeccionesApp:app -b 0.0.0.0:80 --pid gunicorn.pid')
        print("Application started!")

def Stop():
    sudo('kill -9 `cat Proyecto-IV/gunicorn.pid`')
    print("Application stoped!")

def Update():
    with cd("Proyecto-IV"):
		run('git pull')
        run('pip3 install -r requirements.txt')
    print("Application updated!")
