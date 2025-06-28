import json
import os
from time import time, ctime

CONFIG_FILE = "config.json"
VERSIONS_DIR = "form_versions"

def save_config(data):
    try:
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=2)
    except Exception as e:
        print("Error saving config:", e)

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_versioned_forms(form_data):
    os.makedirs(VERSIONS_DIR, exist_ok=True)
    timestamp = time()
    timestr = ctime(timestamp).replace(":", "-").replace(" ", "_")
    filename = os.path.join(VERSIONS_DIR, f"forms_{timestr}.json")
    with open(filename, "w") as f:
        json.dump(form_data, f, indent=2)
