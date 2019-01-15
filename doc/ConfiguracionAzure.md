# Despliegue en Azure

## Herramientas necesarias

**Instalar vagrant**  

Me daba un error al hacer:  
~~~
vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
~~~  


Por lo que lo instalé así:  

~~~
wget -c https://releases.hashicorp.com/vagrant/2.0.3/vagrant_2.0.3_x86_64.deb
sudo dpkg -i vagrant_2.0.3_x86_64.deb
~~~  

como vi aquí: https://github.com/dotless-de/vagrant-vbguest/issues/292


**Instalar ansible**  

Añadir en /etc/apt/sources.list  

~~~
deb http://ppa.launchpad.net/ansible/ansible/ubuntu trusty main
~~~

Ejecutar:  

~~~
$ sudo apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 93C4A3FD7BB9C367
$ sudo apt-get update
$ sudo apt-get install ansible
~~~

[Documentacion Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)  


**Instalar Fabric y su biblioteca**  

~~~
sudo apt-get install fabric
pip install fabric
~~~  


Como a mí me daba problemas al ejecutar el fabfile lo instalé así:  

~~~
pip install fabric==1.13.1
~~~  


[Encontrada solución aquí](https://github.com/tbarbugli/cassandra_snapshotter/issues/123)  



**Instalar el CLI de Azure**  

Prerrequisitos:  

~~~
  sudo apt-get install apt-transport-https lsb-release software-properties-common dirmngr -y
~~~

Modificar lista de las fuentes:  

~~~
AZ_REPO=$(lsb_release -cs)
echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" | \
    sudo tee /etc/apt/sources.list.d/azure-cli.list
~~~  

Obtener la key de Microsoft:  

~~~
  sudo apt-key --keyring /etc/apt/trusted.gpg.d/Microsoft.gpg adv \
       --keyserver packages.microsoft.com \
       --recv-keys BC528686B50D79E339D3721CEB3E94ADBE1229CF
~~~  

Instalar el CLI:  

~~~
  sudo apt-get update
  sudo apt-get install azure-cli
~~~  

[Fuente Original](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-apt?view=azure-cli-latest)  



## Provisionamiento con Ansible  


Para indicarle a nuestro sistema la configuración que necesitamos usamos Ansible. Para hacerlo, crearemos un archivo playbook.yml que es el que se encargará de realizar la tarea.  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/playbook.png)  


Enlace donde explica hosts, become y remote_user. [Documentación](https://docs.ansible.com/ansible/latest/user_guide/playbooks_intro.html#playbook-language-example)  

Me salio un Warning diciendo que usará el module apt en vez de hacer apt-get
Por lo que lo cambié siguiendo esta [documentación](https://docs.ansible.com/ansible/latest/modules/apt_module.html?highlight=apt)  

También cambié el comando de clonar github por el modulo git [aquí](https://docs.ansible.com/ansible/latest/modules/git_module.html?highlight=git)  

Por último, también cambié la manera de instalar los requirements. Haciéndolo
con el modulo pip, siguiendo la [documentación](https://docs.ansible.com/ansible/latest/modules/pip_module.html?highlight=pip3), pero me daba error y lo dejé con command.

## Crear máquina virtual en Azure con Vagrant  


Instalamos plugin de azure para vagrant:  

~~~
vagrant plugin install vagrant-azure
~~~  

Instalamos una base para nuestra máquina del proveedor de azure:  

~~~
vagrant box add azure https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
~~~  


Entramos en nuestra cuenta de Azure ejecutando en nuestra consola:  

~~~
  az login
~~~

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/az_login.png)  


Generamos AAD (Azure Active Directory) que pueda acceder a nuestros recursos en Azure:  
~~~
az ad sp create-for-rbac
~~~  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/az_ad.png)  



**Creamos un Vagrantfile**  

**El vagrantfile lo he copiado de 2 lugares:  
PARTE 1: [vagrant-azure](https://github.com/Azure/vagrant-azure)  
PARTE 2: [vagrant-ansible](https://www.vagrantup.com/docs/provisioning/ansible_intro.html)**  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/vagrantfile.png)  

**Para entender que hace cada línea lo he consultado en los siguientes enlaces:**  
- Vagrant.configure('2') do |config|  
[Documentacion](https://www.vagrantup.com/docs/vagrantfile/version.html)  

- config.vm.box = 'azure'  
[Documentacion](https://www.vagrantup.com/docs/vagrantfile/machine_settings.html)  

- config.ssh.private_key_path = '~/.ssh/id_rsa'  
[Documentacion](https://www.vagrantup.com/docs/vagrantfile/ssh_settings.html)  

- config.vm.provider :azure do |azure|  
[Documentacion](https://www.vagrantup.com/docs/providers/configuration.html)  

Comentar que he quitado el override, de esta línea porque además de no utilizarlo, al final de la documentación recomienda hacerlo sin override siempre que sea posible. De esta forma si se utilizasen más proveedores todos tendrían la misma configuración.


Exportamos variables de Azure  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/export_variables.png)  



Levantamos nuestra máquina:  

~~~
vagrant up --provider=azure
~~~

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/vagrant_up.png)  



Podemos comprobar que se ha creado bien con:  

~~~
vagrant ssh
~~~

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/vagrant_ssh.png)  




Desde el portal de Azure podemos ver los recursos que se han creado:  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/panel.png)  


Datos de la máquina virtual:  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/panel.png)  


Como podemos observar, podemos ver el nombre del dominio y la ip.  



## Despliegue de la aplicación con Fabric  

Con Fabric podremos realizar acciones como lanzar y parar la máquina de una forma mucho más rápida. [Documentación](http://docs.fabfile.org/en/1.14/tutorial.html)  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/fabfile.png)  



Ahora podremos lanzar la aplicación con:  

~~~
fab -f despliegue/fabfile.py -H vagrant@"ip_maquina" "Start"
~~~  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/fab_start.png)  


Ya podemos mirar la aplicación desde el navegador:  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/status.png)  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/peliculas.png)  



Paramos el proceso:  

~~~
fab -f despliegue/fabfile.py -H vagrant@"ip_maquina" "Stop"
~~~  

![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/fab_stop.png)  


El terminal que estaba ejecutando el Start finaliza tras el Stop:  


![img](https://github.com/toniMR/Proyecto-IV/blob/master/doc/img/azure/start_stopping.png)
