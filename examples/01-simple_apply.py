import k8sutils as k8s
import k8sutils.deployments.utils as deployments
import k8sutils.pods.utils as podsutils
import k8sutils.pods as pods

k8s.apply("manifests/nginx.yaml")
deployments.table("nginx")
podsutils.table("nginx")

all_pods = pods.get()

nginx_pods = [pod['metadata']['name'] for pod in all_pods['items'] if 'nginx' in pod['metadata']['name']]
print(nginx_pods)

pods.delete(nginx_pods[0])