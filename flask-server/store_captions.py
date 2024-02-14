import json
import os

def add_captions_to_json(video_id, captions):
    # Check if output.json file exists
    if os.path.exists('output.json'):
        # If file exists, load existing data
        with open('output.json', 'r') as f:
            data = json.load(f)
    else:
        # If file doesn't exist, initialize data
        data = []

    # Append new record
    data.append({"video_id": video_id, "captions": captions})

    # Write data back to JSON file
    with open('output.json', 'w') as f:
        json.dump(data, f, indent=4)

