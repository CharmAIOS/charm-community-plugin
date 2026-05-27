import json
import os

repo = "/Users/ucdream/charm-plugin/charm-community-plugin"

updates = {
    "adapters/registry.json": {
        "adapters": {
            "ag2": "AG2 Multi-Agent",
            "langchain": "LangChain & LangGraph"
        }
    },
    "memory/registry.json": {
        "providers": {
            "redis": "Redis Storage Provider",
            "pinecone": "Pinecone Vector Memory"
        }
    },
    "renderers/registry.json": {
        "renderers": {
            "CRYPTO_CHART": "Crypto Trading Chart"
        }
    },
    "telemetry/registry.json": {
        "exporters": {
            "datadog": "Datadog Telemetry",
            "langsmith": "LangSmith Tracing"
        }
    },
    "templates/registry.json": {
        "templates": {
            "python": "Custom Python Agent",
            "openclaw": "OpenClaw MCP Agent",
            "research-agent": "Web Research Agent",
            "code-review-agent": "Code Review Agent",
            "customer-support-agent": "Customer Support Daemon",
            "data-pipeline-agent": "Data Pipeline Agent",
            "slack-bot": "Slack Workspace Bot"
        }
    },
    "widgets/registry.json": {
        "widgets": {
            "color_picker": "Color Picker Widget"
        }
    }
}

for filepath, mappings in updates.items():
    full_path = os.path.join(repo, filepath)
    if os.path.exists(full_path):
        with open(full_path, 'r') as f:
            data = json.load(f)
            
        for key, arr in data.items():
            if key in mappings and isinstance(arr, list):
                for item in arr:
                    if 'id' in item and item['id'] in mappings[key]:
                        # Insert name right after id
                        # To preserve order if it was ordered, we can just assign
                        item['name'] = mappings[key][item['id']]
                        
        with open(full_path, 'w') as f:
            json.dump(data, f, indent=2)
            print(f"Updated {filepath}")
