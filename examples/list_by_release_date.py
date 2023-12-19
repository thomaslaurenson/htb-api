from datetime import datetime

import numpy as np
import pandas as pd

import config


config = config.Config()

machines_all = list()
machines_all = config.machines_retired + config.machines_active
df = pd.DataFrame.from_dict(machines_all)
df["trophy_room"] = np.where(
    df["name"].isin(config.machines_oscp_normal), True, False)
df = df.sort_values(["release"])

print(f"{'id': <5}{'name':16}{'release':12}{'os':10}{'difficulty'}")
for index, row in df.iterrows():
    # Comment if you want all machines, not just NetSecFocus machines
    if not row["trophy_room"]:
        continue
    machine_id = row["id"]
    name = row["name"]
    release = datetime.strptime(row["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    os = row["os"]
    difficulty = row["difficultyText"]
    print(f"{machine_id: <5}{name:16}{release:12}{os:10}{difficulty}")
