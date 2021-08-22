"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Project data.
"""
import json
from pathlib import Path

import config


with open(f"{config.DATA_PATH}/machines_oscp_normal.json") as f:
    MACHINES_OSCP_NORMAL = json.load(f)

with open(f"{config.DATA_PATH}/machines_oscp_advanced.json") as f:
    MACHINES_OSCP_ADVANCED = json.load(f)

machines_active_path = Path(config.DATA_PATH / "machines_active.json")
machines_retired_path = Path(config.DATA_PATH / "machines_retired.json")
machines_startingpoint_path = Path(
    config.DATA_PATH / "machines_startingpoint.json")
machines_avatars_path = Path(
    config.DATA_PATH / "machines_avatars.json")

if (not machines_active_path.is_file() or
    not machines_retired_path.is_file() or
    not machines_startingpoint_path.is_file() or
        not machines_avatars_path.is_file()):
    print("[*] Warning: Machine JSON file not found! Some scripts might not work.")
    print("[*] You need to use machines/dump_machines.py")
    print("[*] Exiting.")
    exit(1)

with open(machines_active_path) as f:
    MACHINES_ACTIVE = json.load(f)

with open(machines_retired_path) as f:
    MACHINES_RETIRED = json.load(f)

with open(machines_startingpoint_path) as f:
    MACHINES_STARTINGPOINT = json.load(f)

MACHINES_ALL = MACHINES_ACTIVE + MACHINES_RETIRED + MACHINES_STARTINGPOINT

with open(machines_avatars_path) as f:
    MACHINES_AVATARS = json.load(f)
