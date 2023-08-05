from prettytable import PrettyTable
from termcolor import colored

import k8sutils.crds as _crds


def print(highlight=None):
    """Print all CRDs in the cluster. Optionally highlight a CRD by name."""
    crds = _crds.get()
    table = PrettyTable(["Name", "Creation Date"])

    for crd in crds['items']:
        table.add_row([crd['metadata']['name'], crd['metadata']['creationTimestamp']])

    for line in str(table).split("\n"):
        if highlight and highlight in line:
            print(colored(line, 'green'))
        else:
            print(line)
