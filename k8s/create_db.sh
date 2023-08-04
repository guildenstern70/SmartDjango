kubectl apply -f postgres/volume.yaml
kubectl apply -f postgres/volume_claim.yaml
kubectl apply -f postgres/secrets.yaml
kubectl apply -f postgres/deployment.yaml
kubectl apply -f postgres/service.yaml
