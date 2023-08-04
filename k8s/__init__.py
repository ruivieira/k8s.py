import json
import logging
import os
import requests
import subprocess
import tempfile
from urllib.parse import urlparse
from termcolor import colored
from prettytable import PrettyTable


# Configure the logger
logging.basicConfig(level=logging.DEBUG,
                    format="%(asctime)s %(filename)s %(lineno)d> %(message)s",
                    datefmt="%Y-%m-%d %H:%M:%S")


def apply(yaml, namespace=None):
    cmd = f"kubectl apply -f {yaml}"

    if namespace:
        cmd += f" -n {namespace}"

    logging.info(f"Applying {yaml}")
    subprocess.run(cmd, shell=True, check=True)


def pipe_bash(url):
    ua = requests.get(url, stream=True)
    ua.raise_for_status()

    basename = os.path.basename(urlparse(url).path)
    fd, filename = tempfile.mkstemp(prefix=f"{basename}-", dir="/tmp", suffix=".sh")

    with open(fd, 'wb') as out_file:
        out_file.write(ua.content)
    logging.debug(f"Downloaded {url}")

    subprocess.run(f"bash {filename}", shell=True, check=True, capture_output=False)


    os.remove(filename)


def list_crds():
    json_text = subprocess.run("kubectl get crds -o json", shell=True, check=True, capture_output=True, text=True)
    crds = json.loads(json_text.stdout)
    return crds


def print_crds(highlight=None):
    crds = list_crds()
    table = PrettyTable(["Name", "Creation Date"])

    for crd in crds['items']:
        table.add_row([crd['metadata']['name'], crd['metadata']['creationTimestamp']])

    for line in str(table).split("\n"):
        if highlight and highlight in line:
            print(colored(line, 'green'))
        else:
            print(line)


class Kind:
    def __init__(self):
        pass

    @staticmethod
    def create(version='1.26.3', config=None):
        cmd = f"kind create cluster --image=kindest/node:v{version}"

        if config:
            cmd += f" --config='{config}'"

        logging.info(f"Creating a kind cluster with version {version}")
        subprocess.run(cmd, shell=True, check=True)
        subprocess.run('kubectl cluster-info --context kind-kind', shell=True, check=True)

    @staticmethod
    def delete(cluster='kind'):
        logging.info(f"Deleting the kind cluster")
        subprocess.run(f"kind delete cluster --name {cluster}", shell=True, check=True)


class Minikube:
    def __init__(self):
        pass

    @staticmethod
    def start(version='1.26.3', memory=16384, cpus=6):
        cmd = f"minikube start --kubernetes-version=v{version} --memory {memory} --cpus {cpus}"

        logging.info(f"Creating a minikube cluster with version {version}")
        subprocess.run(cmd, shell=True, check=True)
        subprocess.run('minikube addons enable storage-provisioner', shell=True, check=True)
        subprocess.run('minikube addons enable ingress', shell=True, check=True)


def label_namespace(namespace, key, value):
    logging.info(f"Labeling namespace {namespace} with {key}={value}")
    subprocess.run(f"kubectl label namespace {namespace} {key}={value}", shell=True, check=True)


def create_namespace(namespace):
    logging.info(f"Creating namespace {namespace}")
    subprocess.run(f"kubectl create namespace {namespace}", shell=True, check=True)
