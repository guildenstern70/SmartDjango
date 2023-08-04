kubectl delete -f django/service.yaml
kubectl delete -f django/deployment.yaml
kubectl delete -f postgres/service.yaml
kubectl delete -f postgres/deployment.yaml
kubectl delete -f postgres/secrets.yaml
kubectl delete -f postgres/volume_claim.yaml
kubectl delete -f postgres/volume.yaml

