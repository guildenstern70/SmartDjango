kubectl delete -f k8s/django/service.yaml
kubectl delete -f k8s/django/deployment.yaml
kubectl delete -f k8s/postgres/service.yaml
kubectl delete -f k8s/postgres/deployment.yaml
kubectl delete -f k8s/postgres/secrets.yaml
kubectl delete -f k8s/postgres/volume_claim.yaml
kubectl delete -f k8s/postgres/volume.yaml

