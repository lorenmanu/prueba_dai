#-*- mode: ruby -*-
#vi: set ft=ruby :

Vagrant.require_plugin 'vagrant-aws'
Vagrant.require_plugin 'vagrant-omnibus'


Vagrant.configure('2') do |config|
    config.vm.box = "dummy"
    config.vm.box_url = "https://github.com/mitchellh/vagrant-aws/raw/master/dummy.box"
    config.vm.network "public_network"
    config.vm.network "private_network",ip: "192.168.56.10", virtualbox__intnet: "vboxnet0"
    config.vm.network "forwarded_port", guest: 80, host: 80
    config.vm.define "localhost" do |l|
            l.vm.hostname = "localhost"
    end

    config.vm.provider :aws do |aws, override|
        aws.access_key_id = "AKIAIETD7ZLOKLKOBHEQ"
        aws.secret_access_key = "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"
        aws.keypair_name = "prueba"
        aws.ami = "ami-5189a661"
        aws.region = "us-west-2"
        aws.security_groups = "prueba"
        aws.instance_type = "t2.micro"
        override.ssh.username = "ubuntu"
        override.ssh.private_key_path = "./prueba.pem"
    end

    config.vm.provision "ansible" do |ansible|
        ansible.sudo = true
        ansible.playbook = "playbook.yml"
        ansible.verbose = "v"
        ansible.host_key_checking = false
  end
end
