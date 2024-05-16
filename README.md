# Redpanda test

## Summary

### Prerequisites

You should have `kubectl` installed and configured.

### Build

Automated CI/CD builds are triggered when you push changes to GitHub on the
main branch or tag a commit with a version number.

Docker:

```shell
docker build consumer -t redpanda-consumer && docker run --rm redpanda-consumer:latest
docker build producer -t redpanda-producer && docker run --rm redpanda-producer:latest
```

Podman:

```shell
podman build consumer -t redpanda-consumer && podman run --rm redpanda-consumer:latest
podman build producer -t redpanda-producer && podman run --rm redpanda-producer:latest
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

## Development

- release-please
- skaffold
- Conventional commits
