# FastAPI example

## Summary

There is an example manifest `fastapi-example.yaml`.

A simplified/opinionated docker compose configuration is included to demonstrate
the coexistence of it with Kubernetes.

### Prerequisites

You should have `kubectl` installed and configured.

### Build

Automated CI/CD builds are triggered when you push changes to GitHub on the
main branch or tag a commit with a version number.

### Deploy

Apply the manifests:

```shell
kubectl apply -f fastapi-example.yaml
```

## Upgrading dependencies

```shell
pdm update
```
