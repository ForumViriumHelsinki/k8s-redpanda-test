# Redpanda test

## Summary

### Prerequisites

You should have `kubectl` installed and configured.

### Build

Automated CI/CD builds are triggered when you push changes to GitHub on the
main branch or tag a commit with a version number.

```shell
docker build consumer -t redpanda-consumer
docker build producer -t redpanda-producer
```

### Deploy

Apply the manifests:

```shell
kubectl apply -f redpanda-test.yaml
```

## Upgrading dependencies

```shell
uv venv
uv pip sync
```
