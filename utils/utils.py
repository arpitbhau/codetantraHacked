# Jai Shree Ram

import json

def readJsonFile(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)
