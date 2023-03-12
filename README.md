# An example of a Kubernetes microservice with automatic TLS certificate creation/renewal

## Install certificate manager

```
helm repo add jetstack https://charts.jetstack.io
helm repo update
helm install cert-manager jetstack/cert-manager --namespace cert-manager --create-namespace --version v1.11.0 --set installCRDs=true
```

## Install LetsEncrypt cluster issuer

```
kubectl apply -f helm/charts/cert-manager/cert-issuer-production.yaml
```

## Install nginx ingress controller

```
helm repo add nginx-stable https://helm.nginx.com/stable
helm repo update
helm install nginx-ingress nginx-stable/nginx-ingress -n nginx-ingress
```

## Install application helm chart

```
helm install tamedia-app helm/charts/tamedia-app -f helm/values/dev/tamedia-app.yaml --namespace tamedia --create-namespace
```
