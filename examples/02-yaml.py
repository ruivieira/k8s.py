#!/usr/bin/env python3
from k8sutils import Yaml

yaml = Yaml("manifests/nginx.yaml")

yaml.set("spec.replicas", 2)
yaml.set("spec.template.spec.containers[0].image", "nginx:1.19.6")
yaml.save("manifests/nginx-edited.yaml")