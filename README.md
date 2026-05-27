# Charm Community Plugins

Welcome to the central registry for community-developed Charm plugins! 

This repository powers the discovery of plugins inside the Charm Store. By submitting your plugin here, it becomes visible to all developers using Charm.

## How to submit a Custom Runtime

To make your custom Docker image discoverable to the Charm ecosystem:

1. Fork this repository.
2. Edit `runtimes/registry.json` to add your image.
3. Submit a Pull Request.

### Requirements
- Your entry must conform to `schemas/runtime.schema.json`.
- The `image` must be publicly accessible (e.g., GHCR, Docker Hub).
- The `image` must be built for `linux/amd64` architecture.
- The `image` must extend the official Charm base images.
