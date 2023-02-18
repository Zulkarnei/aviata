# main logic
import json


def extract_data(path_to_files):
    with open(path_to_files, 'r') as f:
        data = json.load(f)
    return data
