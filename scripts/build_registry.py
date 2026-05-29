import os
import json
import glob

def build_category(category_name, key_name, is_list=False):
    manifest_files = glob.glob(f"{category_name}/manifests/*.json")
    items = []
    
    for mf in manifest_files:
        if os.path.basename(mf) == "_example.json":
            continue
        with open(mf, "r", encoding="utf-8") as f:
            data = json.load(f)
            items.append(data)
            
    if is_list:
        registry_data = items
    else:
        registry_data = {
            "version": "1.0",
            key_name: items
        }
    
    with open(f"{category_name}/registry.json", "w", encoding="utf-8") as f:
        json.dump(registry_data, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Built {category_name}/registry.json with {len(items)} items.")

def main():
    build_category("adapters", "adapters")
    build_category("memory", "providers")
    build_category("renderers", "renderers")
    build_category("runtimes", "runtimes", is_list=True)
    build_category("telemetry", "exporters")
    build_category("templates", "templates")
    build_category("widgets", "widgets")

if __name__ == "__main__":
    main()
