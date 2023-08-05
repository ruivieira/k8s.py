import k8sutils as k8s
import k8sutils.deployments.utils as deployments

k8s.apply("manifests/nginx.yaml")
deployments.table("nginx")