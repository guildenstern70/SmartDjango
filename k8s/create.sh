kubectl apply -f k8s/postgres/volume.yaml
kubectl apply -f k8s/postgres/volume_claim.yaml
kubectl apply -f k8s/postgres/secrets.yaml
kubectl apply -f k8s/postgres/deployment.yaml
kubectl apply -f k8s/postgres/service.yaml
kubectl apply -f k8s/django/deployment.yaml
kubectl apply -f k8s/django/service.yaml
