import sys
import json


with open(sys.argv[1]) as f:
    items = json.load(f)
    items["rows"].sort(key=lambda x: x["version"])
    sys.stdout.write(json.dumps(items, sort_keys=True, indent=4))
