# PARTE 1
# Copiado de https://github.com/Azure/vagrant-azure
# ---------------------------------------------------------
# Actualmente, solo hay dos versiones compatibles: "1" y "2".
# La versión 1 representa la configuración de Vagrant 1.0.x.
# "2" representa la configuración para 1.1+ hasta a 2.0.x.

# Indico que uso la 2 porque en la version 1 no se puede usar
# config.vm.provider
Vagrant.configure('2') do |config|

  # Configura la 'box' en la que se traerá la máquina.
  # El nombre del 'box' es el que le dimos cuando hicimos
  # vagrant box add 'nombre' https://github.com/azure/vagrant-azure/raw/v2.0/dummy.box --provider azure
  config.vm.box = 'azure'

  # Configurar ruta a la clave privada para conectar remotamente
  # al vagrant box
  config.ssh.private_key_path = '~/.ssh/id_rsa'

  # Establece la configuración de la máquina para un proveedor específico
  # Crea una variable, en mi caso llamada azure para realizar la configuración
  config.vm.provider :azure do |azure|

    # Parámetros para los datos de la suscripción de Azure
    # Establece variables de entorno para poder asignarles el valor
    azure.tenant_id = ENV['AZURE_TENANT_ID']
    azure.client_id = ENV['AZURE_CLIENT_ID']
    azure.client_secret = ENV['AZURE_CLIENT_SECRET']
    azure.subscription_id = ENV['AZURE_SUBSCRIPTION_ID']

    # Nombre de la máquina virtual
    azure.vm_name = "proyeccionescine"

    # Nombre de usuario del administrador de la Máquina Virtual
    azure.admin_username = "toniMR"

    # Puerto por el que nos conectaremos a la máquina
    azure.tcp_endpoints = '80'
  end

# PARTE 2
# Copiado de https://www.vagrantup.com/docs/provisioning/ansible.html
# ---------------------------------------------------------

  # Establece la configuración para realizar el provisionamiento
  config.vm.provision :ansible do |ansible|
    # Indica la ruta en la que encuentra el archivo playbook.yml
    ansible.playbook = "provision/playbook.yml"
  end
end
