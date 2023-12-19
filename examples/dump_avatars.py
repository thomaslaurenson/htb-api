import json

import config
import htb


config = config.Config()

htb = htb.HTB()
if config.token:
    htb.set_token(config.token)
else:
    htb.get_token(config.email, config.password)

machines_all = list()
machines_all = config.machines_retired + config.machines_active

machines_all = sorted(machines_all, key=lambda i: i["id"])

for machine in machines_all:
    machine_id = str(machine["id"])

    # Load avatar file for each loop iteration
    # This allows updating inline
    with open(f"{config.data_path}/machines_avatars.json") as f:
        machines_avatars = json.load(f)

    if machine_id in machines_avatars:
        print(f"[*] Skipping machine ID: {machine_id}")
        continue
    else:
        print(f"[*] Downloading machine ID: {machine_id}")

    avatar_url = machine["avatar"]
    img_b64_str = htb.get_avatar(avatar_url)

    machines_avatars[machine_id] = img_b64_str

    # Dump image data to JSON file
    with open(f"{config.data_path}/machines_avatars.json", "w") as f:
        json.dump(machines_avatars, f, indent=4)
