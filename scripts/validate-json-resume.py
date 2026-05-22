#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "jsonschema",
#   "requests",
# ]
# ///

import json
import sys
import requests
import jsonschema

SCHEMA_URL = "https://raw.githubusercontent.com/jsonresume/resume-schema/master/schema.json"
RESUME_PATH = "manual/resume.json"

def main():
    print(f"Fetching schema from {SCHEMA_URL}...")
    schema = requests.get(SCHEMA_URL, timeout=10).json()

    print(f"Loading {RESUME_PATH}...")
    with open(RESUME_PATH, encoding="utf-8") as f:
        resume = json.load(f)

    print("Validating...")
    try:
        jsonschema.validate(instance=resume, schema=schema)
        print("✓ resume.json is valid")
    except jsonschema.ValidationError as e:
        print(f"✗ Validation error: {e.message}")
        print(f"  Path: {' -> '.join(str(p) for p in e.absolute_path)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
