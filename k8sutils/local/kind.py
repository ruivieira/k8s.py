import logging
import subprocess


def start(name='kind', version='1.26.3'):
    """Start a kind cluster"""
    logging.info(f"Creating a kind cluster '{name}' with version {version}")

    cmd = f"kind create cluster --name {name} --image kindest/node:v{version}"
    subprocess.run(cmd, shell=True, check=True)


def delete(name='kind'):
    """Delete a kind cluster"""
    logging.info(f"Deleting kind cluster '{name}'")
    cmd = f"kind delete cluster --name {name}"
    subprocess.run(cmd, shell=True, check=True)
