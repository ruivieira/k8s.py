import k8sutils as k8s
import k8sutils.deployments.utils as deployments
import k8sutils.pods.utils as pods

k8s.apply("manifests/nginx.yaml")
deployments.table("nginx")
pods.table("nginx")