#!/usr/bin/env python
import git
import os
import requests
import tarfile
import subprocess
import time
from colorama import init, Fore, Back, Style

git_url = "https://github.com/bigpandaio/ops-exercise"
image_dir = "public/images"
pics_url = "https://s3.eu-central-1.amazonaws.com/devops-exercise/pandapics.tar.gz"
project_dir = git_url.split('/')[-1]
tar_name = pics_url.split('/')[-1]
health_check_url = "http://localhost:3000/health"

def cprint(msg, foreground = "black", background = "white"):
    fground = foreground.upper()
    bground = background.upper()
    style = getattr(Fore, fground) + getattr(Back, bground)
    print(style + msg + Style.RESET_ALL)

def git_clone(git_url, project_dir):
    if not os.path.exists(project_dir):
        git.Repo.clone_from(git_url, project_dir, branch='master', recursive=True)
        cprint ("Cloned repo: %s successfully!" % git_url, "blue", "black")

def download_extract_tar(pics_url, project_dir, image_dir, tar_name):
    if not os.path.isfile(tar_name):
        response = requests.get(pics_url, allow_redirects=True)
        open(tar_name, 'wb').write(response.content)
        cprint("Downloaded file: %s successfully!" % tar_name, "magenta", "black")
    tar = tarfile.open(tar_name, "r:gz")
    tar.extractall(project_dir + '/' + image_dir)
    tar.close()
    cprint("Extracted file: %s successfully!" % tar_name, "cyan", "black")

def run_docker_compose():
    subprocess.call(['docker-compose', 'up', '--build', '-d'])
    cprint("Runed docker-compose successfully!", "blue", "black")

def health_check(health_check_url):
    cprint("Checking %s" %health_check_url, "yellow", "black")
    healthcheck = requests.get(health_check_url)
    if healthcheck.status_code == 200:
        cprint("Deployment finished successfully!", "green", "black")
    else:
        cprint("Deployment was failed!", "red", "black")

if __name__ == '__main__':
    git_clone(git_url, project_dir)
    download_extract_tar(pics_url, project_dir, image_dir, tar_name)
    run_docker_compose()
    time.sleep(5)
    health_check(health_check_url)
