"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: List HTB machines by release date.
"""
import json
from datetime import datetime

import numpy as np
import pandas as pd

import config


# Load all the JSON files
with open(f"{config.DATA_PATH}/machines_target_list.json") as f:
    machines_target = json.load(f)
with open(f"{config.DATA_PATH}/machines_advanced_list.json") as f:
    machines_advanced = json.load(f)
with open(f"{config.DATA_PATH}/machines_active.json") as f:
    machines_active = json.load(f)
    machines_active = machines_active["info"]
with open(f"{config.DATA_PATH}/machines_retired.json") as f:
    machines_retired = json.load(f)
    machines_retired = machines_retired["info"]

# Load DF from JSON
machines_all = list()
machines_all = machines_retired + machines_active
df = pd.DataFrame.from_dict(machines_all)

# Add new column if the machine is in Trophy Room list
df["trophy_room"] = np.where(df["name"].isin(machines_target), True, False)

df = df.sort_values(["release"])

print(f"{'id': <5}{'name':16}{'release':12}{'os':10}{'difficulty'}")
for index, row in df.iterrows():
    # Comment line if you want all machines
    # not just NetSecFocus Trophy room machines
    # if not row["trophy_room"]:
    #     continue

    machine_id = row["id"]
    name = row["name"]
    release = datetime.strptime(row["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    os = row["os"]
    difficulty = row["difficultyText"]

    print(f"{machine_id: <5}{name:16}{release:12}{os:10}{difficulty}")
