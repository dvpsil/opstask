#!/bin/sh
set -eu

# Install docker
sudo wget -qO- https://get.docker.com/ | sh
printf '\nDocker installed successfully\n\n'

# Install docker-compose
COMPOSE_VERSION=`git ls-remote https://github.com/docker/compose | grep refs/tags | grep -oP "[0-9]+\.[0-9][0-9]+\.[0-9]+$" | tail -n 1`
sudo sh -c "curl -L https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose"
sudo chmod +x /usr/local/bin/docker-compose
sudo sh -c "curl -L https://raw.githubusercontent.com/docker/compose/${COMPOSE_VERSION}/contrib/completion/bash/docker-compose > /etc/bash_completion.d/docker-compose"
printf '\nDocker-compose installed successfully\n\n'

# Install python modules
sudo apt --yes install python-git python-colorama python-requests python3-git python3-colorama python3-requests
printf '\nPython modules installed successfully\n\n'
