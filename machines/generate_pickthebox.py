"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Generate the JSON files for pickabox web app.
"""
import json
from datetime import datetime

import config
import data


machine_metadata = list()


def is_retired(machine_id: str) -> bool:
    for machine in data.MACHINES_RETIRED:
        if machine["id"] == machine_id:
            return True
    return False


pickabox_data = list()

for machine in data.MACHINES_ALL:
    machine_dict = dict()
    machine_dict["id"] = machine["id"]
    machine_dict["name"] = machine["name"]
    os = machine["os"]
    if os in ["OpenBSD", "FreeBSD", "Solaris", "Android"]:
        os = "Other"
    machine_dict["os"] = os
    release = datetime.strptime(machine["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    machine_dict["release"] = release.strftime("%Y-%m-%d")
    machine_dict["difficulty"] = machine["difficultyText"]
    machine_dict["free"] = machine["free"]
    machine_dict["recommended"] = True if machine["recommended"] == 1 else False
    machine_dict["retired"] = is_retired(machine["id"])
    machine_dict["startingpoint"] = True if machine["sp_flag"] == 1 else False
    machine_dict["oscp_normal"] = True if machine["name"] in data.MACHINES_OSCP_NORMAL else False
    machine_dict["oscp_advanced"] = True if machine["name"] in data.MACHINES_OSCP_ADVANCED else False
    pickabox_data.append(machine_dict)

pickabox_data = sorted(pickabox_data, key = lambda i: i["release"], reverse=True)

with open(f"{config.DATA_PATH}/machines_data.json", "w") as f:
    json.dump(pickabox_data, f, indent=4)
