# Redpanda test

## Summary

Redpanda testing

## Development

- Prerequisites
    - Skaffold
        - Skaffold handles the workflow for building, pushing and deploying
        your application, allowing you to focus on what matters most: writing
        code
    - Docker Desktop Kubernetes, minikube or k3d for running the services on
    your workstation using skaffold
- Run `skaffold dev`
    - Skaffold will build images, deploy the service stack and watch for changes
- Make changes to code 
    - Skaffold will re-build and re-deploy when changes are detected
- Commit & push
    - Use Conventional commits
- Create pull request
- Merge pull request to main (use rebase or squash)
- release-please will create pull requests for new releases based on commits
- New releases are deployed automatically
