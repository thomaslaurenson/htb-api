import json
from datetime import datetime

import config


def is_retired(machine_id: str) -> bool:
    for machine in config.machines_retired:
        if machine["id"] == machine_id:
            return True
    return False


config = config.Config()
machine_metadata = list()
pickabox_data = list()

machines_all = list()
machines_all = config.machines_retired + config.machines_active

for machine in machines_all:
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
    machine_dict["oscp_normal"] = True if machine["name"] in config.machines_oscp_normal else False
    machine_dict["oscp_advanced"] = True if machine["name"] in config.machines_oscp_advanced else False
    pickabox_data.append(machine_dict)

pickabox_data = sorted(pickabox_data, key=lambda i: i["release"], reverse=True)

with open(f"{config.data_path}/machines_data.json", "w") as f:
    json.dump(pickabox_data, f, indent=4)
