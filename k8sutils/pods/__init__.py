import json
import subprocess

def get(namespace=None):
    """Get all pods in the cluster"""
    cmd = "kubectl get pods -o json"
    if namespace:
        cmd += f" -n {namespace}"

    result = subprocess.run(cmd, shell=True, check=True, capture_output=True, text=True)
    pods = json.loads(result.stdout)
    return pods
