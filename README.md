Bigpanda's Ops task.

## Installation
Clone this repo
```
git clone https://github.com/dvpsil/opstask.git
cd opstask
sh install.sh
python deployment_flow.py
```

## Files

  - install.sh - Script to install docker, docker-compose and python modules on Ubuntu.
    ## Usage
    `sh install.sh`

  - deployment_flow.py - The deployment flow script, coded using Python language (support python 2.7 and 3)
    ## Usage
    `python deployment_flow.py`

  - docker-compose.yml - This Compose file defines two services, App and DB.
    ## Usage
    `docker-compose up -d`
