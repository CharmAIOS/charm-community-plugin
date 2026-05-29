# Charm Community Plugins

Welcome to the central registry for community-developed Charm plugins! 

This repository powers the discovery of plugins inside the Charm Store. By submitting your plugin here, it becomes visible to all developers using Charm.

## Plugin Schema Guidelines

When submitting a plugin to any of the categories below, your JSON entry must follow a standardized schema. This ensures the Charm Store can accurately display your plugin with rich UI features (like sorting, nice visuals, and detailed views).

### Required Fields
- `id`: `string` (Unique identifier, e.g., `"redis"`. Used to generate configuration or install commands)
- `name`: `string` (Display name for the UI, e.g., `"Charm Redis Memory"`)
- `description`: `string` (A short paragraph describing your plugin)
- `author`: `string` (Author or organization name, e.g., `"Charm Team"`)
- `tags`: `string[]` (Array of tags, e.g., `["database", "kv"]` for search filtering)
- `github_url`: `string` (URL to the plugin's source code)

### Recommended Fields (for advanced Store UI features)
- `version`: `string` (Current version, e.g., `"1.0.0"`)
- `docs_url`: `string` (URL to official documentation)
- `license`: `string` (e.g., `"MIT"`)
- `pypi_package` / `npm_package`: `string` (Used for generating install commands)

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

## How to submit a Telemetry Exporter

To share your observability integration (e.g., Datadog, LangSmith, Sentry) with the community:

1. Use the [charm-telemetry-template](https://github.com/CharmAIOS/charm-telemetry-template) to bootstrap your project.
2. Publish your telemetry package to PyPI.
3. Fork this repository.
4. Edit `telemetry/registry.json` to add your package details.
5. Submit a Pull Request.

Once merged, your telemetry exporter will instantly appear in the Charm Store.

## How to submit a Memory Storage Plugin

To share your state and memory backend (e.g., Redis, MongoDB, Pinecone) with the community:

1. Use the [charm-memory-template](https://github.com/CharmAIOS/charm-memory-template) to bootstrap your project.
2. Publish your memory package to PyPI.
3. Fork this repository.
4. Edit `memory/registry.json` to add your package details.
5. Submit a Pull Request.

Once merged, your memory plugin will instantly appear in the Charm Store.

## How to submit an Output Renderer Plugin

To share a custom UI widget or chart (e.g., custom stock chart, data grid) for the Store Frontend:

1. Create a React component that takes a `payload` prop and export it as the default export.
2. Publish your React component package to NPM (ensure it is ESM compatible).
3. Fork this repository.
4. Edit `renderers/registry.json` to add your package details (`id` matches the `_charm_render_type`).
5. Submit a Pull Request.

Once merged, your output renderer will be dynamically loaded by the Charm Store whenever an agent emits your render type.

## How to submit an Input UI Widget Plugin

To share a custom configuration field (e.g., custom color picker, slider, or code editor) for the Store Frontend:

1. Create a React component that implements the `FieldProps` interface and export it as the default export.
2. Publish your React component package to NPM (ensure it is ESM compatible).
3. Fork this repository.
4. Edit `widgets/registry.json` to add your package details (`id` matches the `ui:widget` value).
5. Submit a Pull Request.

Once merged, your input widget will be dynamically loaded by the Charm Store whenever an agent uses your `ui:widget` in their `charm.yaml` settings schema.
