"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: List HTB machines by release date.
"""
from datetime import datetime

import numpy as np
import pandas as pd

import data


# Load DF from JSON
machines_all = list()
machines_all = data.MACHINES_RETIRED + data.MACHINES_ACTIVE
df = pd.DataFrame.from_dict(machines_all)

# Add new column if the machine is in Trophy Room list
df["trophy_room"] = np.where(
    df["name"].isin(data.MACHINES_OSCP_NORMAL), True, False)

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
