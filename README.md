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

## How to Submit a Plugin

We use a "One File Per Plugin" manifest system to avoid Git merge conflicts. To submit a plugin or template:

1. Fork this repository.
2. Find the relevant category folder (e.g., `adapters/`, `memory/`, `templates/`).
3. Inside the `manifests/` folder, copy the `_example.json` file and rename it to your plugin's ID (e.g., `adapters/manifests/my_plugin.json`).
4. Fill out the JSON file according to the schema requirements.
5. Submit a Pull Request.

Once your Pull Request is merged into `main`, our GitHub Actions will automatically compile your manifest into the central `registry.json` and it will instantly appear in the Charm Store!

### Custom Runtimes
- Category Folder: `runtimes/manifests/`
- Schema: `schemas/runtime.schema.json`
- The `image` must be built for `linux/amd64` architecture and extend the official Charm base images.

### Agent Templates
- Category Folder: `templates/manifests/`
- Schema: `schemas/template.schema.json`
- Convert your project files into the required JSON structure.

### Custom Adapters
- Category Folder: `adapters/manifests/`
- Schema: `schemas/adapter.schema.json`
- You must publish your adapter package to PyPI first.

### Telemetry Exporters
- Category Folder: `telemetry/manifests/`
- Schema: `schemas/telemetry.schema.json`
- You must publish your telemetry package to PyPI first.

### Memory Storage Plugins
- Category Folder: `memory/manifests/`
- Schema: `schemas/memory.schema.json`
- You must publish your memory package to PyPI first.

### Output Renderer Plugins
- Category Folder: `renderers/manifests/`
- Schema: `schemas/renderers.schema.json`
- You must publish your React component package to NPM first (ensure it is ESM compatible).

### Input UI Widget Plugins
- Category Folder: `widgets/manifests/`
- Schema: `schemas/widgets.schema.json`
- You must publish your React component package to NPM first (ensure it is ESM compatible).
