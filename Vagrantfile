# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
 

  config.vm.box = "ubuntu/trusty64"
  # config.vm.box_check_update = false
   config.vm.network "forwarded_port", guest: 8100, host: 8100
  # config.vm.network "private_network", ip: "192.168.33.10"
  # config.vm.network "public_network"
  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provision "shell", inline: <<-SHELL
     sudo apt-get update
     sudo apt-get upgrade
     sudo apt-get install python-pip -y
     sudo apt-get install python-dev -y
     sudo apt-get install git -y
     git config --global user.name "Jeff Reiher"
    git config --global user.email "jreiher2003@yahoo.com"
    git config --global push.default upstream
    git config --global merge.conflictstyle diff3
    git config --global credential.helper 'cache --timeout=10000'
    wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-completion.bash
    wget https://raw.githubusercontent.com/git/git/master/contrib/completion/git-prompt.sh
    wget https://www.udacity.com/api/nodes/3333158951/supplemental_media/bash-profile-course/download
    cat download >> .bashrc
    rm download
   SHELL
end
