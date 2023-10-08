from datetime import datetime

import pandas as pd

import data


# Load DF from JSON
df = pd.DataFrame.from_dict(data.MACHINES_ACTIVE)

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
