from fabric.api import run, cd, sudo

def Start():
    with cd("Proyecto-IV/src/"):
        sudo('gunicorn proyeccionesApp:app -b 0.0.0.0:80')
        print("Application started!")

def Stop():
    sudo("pkill gunicorn")
    print("Application stoped!")

def Update():
    with cd("Proyecto-IV"):
        run('git pull')
        run('pip3 install -r requirements.txt')
        print("Application updated!")
