"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Generate the tables for my trophy_room project README file.
"""
from pathlib import Path

import config
import data


# Make machine lookup dict
machines_retired_lookup = dict()
for machine in data.MACHINES_RETIRED:
    machines_retired_lookup[machine["name"].lower()] = machine
machines_startingpoint_lookup = dict()
for machine in data.MACHINES_STARTINGPOINT:
    machines_startingpoint_lookup[machine["name"].lower()] = machine

# Find all machines with a writeup
try:
    p = Path(f"{config.TROPHY_ROOM_PATH}/machines").glob('*')
except AttributeError:
    print("[*] Uncomment TROPHY_ROOM_PATH in config.py...")
    exit(1)

machines_completed = [x.stem for x in p if x.is_dir()]
machines_completed.sort()

# Machines: Generate a nice table for the README file
print("| Name | System | Difficulty | Trophy List |")
print("| ---- |--------|------------|-------------|")
for machine_name in machines_completed:
    machine_data = machines_retired_lookup[machine_name]
    name = machine_data["name"]
    url = f"hackthebox/machines/{machine_name}"
    os = machine_data["os"]
    difficulty = machine_data["difficultyText"]

    if name in data.MACHINES_OSCP_NORMAL:
        trophy_list = "Yes"
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} |")

# Find all starting point machines with a writeup
p = Path(f"{config.TROPHY_ROOM_PATH}/startingpoint").glob('*')
machines_completed = [x.stem for x in p if x.is_dir()]
machines_completed.sort()

# Starting Point: Generate a nice table for the README file
print("| Name | System | Difficulty | Trophy List |")
print("| ---- |--------|------------|-------------|")
for folder_name in machines_completed:
    # Skip creds dir
    if folder_name == "creds":
        continue
    # Remove starting point name prefix
    machine_name = folder_name[2:]
    machine_data = machines_startingpoint_lookup[machine_name]
    name = machine_data["name"]
    url = f"hackthebox/startingpoint/{folder_name}"
    os = machine_data["os"]
    difficulty = machine_data["difficultyText"]

    if name in data.MACHINES_OSCP_NORMAL:
        trophy_list = "Yes"
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} |")
