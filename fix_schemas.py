import glob
import json

for f in glob.glob("schemas/*.schema.json"):
    with open(f, "r") as file:
        schema = json.load(file)
        
    if schema.get("type") == "array" and "items" in schema:
        inner_schema = schema["items"]
    elif schema.get("type") == "object" and "properties" in schema:
        list_keys = [k for k in schema["properties"].keys() if k != "version"]
        if not list_keys:
            continue
        list_key = list_keys[0]
        if "items" in schema["properties"][list_key]:
            inner_schema = schema["properties"][list_key]["items"]
        else:
            continue
    else:
        print(f"Skipping {f}")
        continue
        
    inner_schema["$schema"] = schema.get("$schema", "http://json-schema.org/draft-07/schema#")
    inner_schema["title"] = schema.get("title", f"Charm Plugin Item")
    
    with open(f, "w") as file:
        json.dump(inner_schema, file, indent=2)
        file.write("\n")
    print(f"Updated {f}")
