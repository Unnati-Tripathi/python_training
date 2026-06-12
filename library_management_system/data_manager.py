import json
import os
from datetime import datetime, timedelta

DATA_FILE = "library_data.json"

def load_data():
    if not os.path.exists(DATA_FILE):
        return {"books": {}, "users": {}, "transactions": []}
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

def initialize_data():
    if not os.path.exists(DATA_FILE):
        save_data({"books": {}, "users": {}, "transactions": []})
