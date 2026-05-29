import os
import json

categories = ["adapters", "memory", "renderers", "runtimes", "telemetry", "templates", "widgets"]

for cat in categories:
    reg_file = f"{cat}/registry.json"
    if not os.path.exists(reg_file):
        continue
    
    with open(reg_file, "r") as f:
        data = json.load(f)
        
    if isinstance(data, list):
        items = data
    else:
        list_keys = [k for k in data.keys() if k != "version"]
        if not list_keys:
            items = []
        else:
            list_key = list_keys[0]
            items = data[list_key]
    
    manifests_dir = f"{cat}/manifests"
    os.makedirs(manifests_dir, exist_ok=True)
    
    if cat == "templates":
        for item in items:
            item_id = item.get("id", "unknown")
            with open(f"{manifests_dir}/{item_id}.json", "w") as f:
                json.dump(item, f, indent=2)
                f.write("\n")
        if items:
            example = items[0].copy()
            example["id"] = "example-template"
            with open(f"{manifests_dir}/_example.json", "w") as f:
                json.dump(example, f, indent=2)
                f.write("\n")
    else:
        if len(items) > 0:
            example_item = items[0].copy()
            example_item["id"] = "example-plugin"
            if "name" in example_item:
                example_item["name"] = "Example Plugin"
            with open(f"{manifests_dir}/_example.json", "w") as f:
                json.dump(example_item, f, indent=2)
                f.write("\n")
                
print("Migration completed.")
