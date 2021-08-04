"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: List active HTB machines.
"""
import json
from datetime import datetime

import pandas as pd

import config


# Load all the JSON files
with open(f"{config.DATA_PATH}/machines_active.json") as f:
    machines_active = json.load(f)
    machines_active = machines_active["info"]

# Load DF from JSON
df = pd.DataFrame.from_dict(machines_active)

df = df.sort_values(["release"])

print(f"{'id': <5}{'name':16}{'release':12}{'os':10}{'difficulty'}")
for index, row in df.iterrows():
    machine_id = row["id"]
    name = row["name"]
    release = datetime.strptime(row["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    os = row["os"]
    difficulty = row["difficultyText"]

    print(f"{machine_id: <5}{name:16}{release:12}{os:10}{difficulty}")
