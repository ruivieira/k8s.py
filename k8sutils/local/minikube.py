import logging
import subprocess


def start(version='1.26.3', memory=16384, cpus=6):
    """Start a minikube cluster"""
    cmd = f"minikube start --kubernetes-version=v{version} --memory {memory} --cpus {cpus}"

    logging.info(f"Creating a minikube cluster with version {version}")
    subprocess.run(cmd, shell=True, check=True)
    subprocess.run('minikube addons enable storage-provisioner', shell=True, check=True)
    subprocess.run('minikube addons enable ingress', shell=True, check=True)


def delete():
    """Delete a minikube cluster"""
    logging.info(f"Deleting minikube cluster")
    cmd = f"minikube delete"
    subprocess.run(cmd, shell=True, check=True)
