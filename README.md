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

## How to submit an Agent Template

To share your starter template with the community:

1. Fork this repository.
2. Convert your project files into a single JSON entry following the structure in `templates/registry.json`.
3. Append your entry to the `templates` array.
4. Submit a Pull Request.

Once merged, your template will instantly appear in the Charm Store and become available via `charm init --template <your-template-id>`.

## How to submit a Custom Adapter

To share your framework adapter (e.g., LangChain, AG2, Autogen) with the community:

1. Use the [charm-adapter-template](https://github.com/CharmAIOS/charm-adapter-template) to bootstrap your project.
2. Publish your adapter package to PyPI.
3. Fork this repository.
4. Edit `adapters/registry.json` to add your package details.
5. Submit a Pull Request.

Once merged, your adapter will instantly appear in the Charm Store and become discoverable for `uv pip install`.
