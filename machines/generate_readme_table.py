"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Generate the tables for my trophy_room project README file.
"""
from pathlib import Path
from datetime import datetime

import config
import data


PUBLISHED_DATE_LOOKUP = {
    "Bashed": "2021-06-27",
    "Shocker": "2021-06-27",
    "Lame": "2021-06-27",
    "Nibbles": "2021-07-03",
    "Beep": "2021-07-03",
    "Cronos": "2021-07-04",
    "Nineveh": "2021-07-06",
    "Archetype": "2021-07-08",
    "Oopsie": "2021-07-10",
    "Vaccine": "2021-07-11",
    "Sense": "2021-07-16",
    "Spectra": "2021-07-21",
    "Legacy": "2021-07-25",
    "Devel": "2021-07-25",
    "Popcorn": "2021-07-26",
    "Armageddon": "2021-07-26",
    "Shield": "2021-07-29",
    "TheNotebook": "2021-07-03",
    "Writeup": "2021-08-04",
    "OpenAdmin": "2021-08-05",
    "Love": "2021-08-14",
    "Tabby": "2021-08-18",
    "Ophiuchi": "2021-08-19",
    "Jerry": "2021-08-20",
    "Knife": "2021-08-30",
}


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
print("| Name | System | Difficulty | Trophy List | Release Date | Published Date |")
print("| ---- |--------|------------|-------------|--------------|----------------|")
for machine_name in machines_completed:
    machine_data = machines_retired_lookup[machine_name]
    name = machine_data["name"]
    url = f"hackthebox/machines/{machine_name}"
    os = machine_data["os"]
    difficulty = machine_data["difficultyText"]
    release = datetime.strptime(machine_data["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    published = PUBLISHED_DATE_LOOKUP[name]

    if name in data.MACHINES_OSCP_NORMAL:
        trophy_list = "Yes"
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} | {release} | {published} |")

# Find all starting point machines with a writeup
p = Path(f"{config.TROPHY_ROOM_PATH}/startingpoint").glob('*')
machines_completed = [x.stem for x in p if x.is_dir()]
machines_completed.sort()

# Starting Point: Generate a nice table for the README file
print("| Name | System | Difficulty | Trophy List | Release Date | Published Date |")
print("| ---- |--------|------------|-------------|--------------|----------------|")
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
    release = datetime.strptime(machine_data["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    published = PUBLISHED_DATE_LOOKUP[name]

    if name in data.MACHINES_OSCP_NORMAL:
        trophy_list = "Yes"
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} | {release} | {published} |")
