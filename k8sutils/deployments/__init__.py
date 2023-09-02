import json
import subprocess

from k8sutils.annotations import rethrow


@rethrow
def get(namespace=None):
    """Get all deployments in the cluster"""
    cmd = "kubectl get deployments -o json"
    if namespace:
        cmd += f" -n {namespace}"

    result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    deployments = json.loads(result.stdout)
    return deployments
