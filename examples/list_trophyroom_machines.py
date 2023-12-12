from datetime import datetime

import numpy as np
import pandas as pd

import config


config = config.Config()

df = pd.DataFrame.from_dict(config.machines_retired)
df["trophy_room"] = np.where(
    df["name"].isin(config.machines_oscp_normal), True, False)
df["trophy_room_adv"] = np.where(
    df["name"].isin(config.machines_oscp_advanced), True, False)
df = df.sort_values(["release"])

print(f"{'id': <5}{'name':16}{'release':12}{'os':10}{'difficulty':12}{'status'}")
for index, row in df.iterrows():
    machine_id = row["id"]
    name = row["name"]
    release = datetime.strptime(row["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    os = row["os"]
    difficulty = row["difficultyText"]
    if row["trophy_room"]:
        print(f"{machine_id: <5}{name:16}{release:12}{os:10}{difficulty:12}{'Normal'}")
    if row["trophy_room_adv"]:
        print(f"{machine_id: <5}{name:16}{release:12}{os:10}{difficulty:12}{'Advanced'}")
