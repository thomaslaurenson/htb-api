import json

import config
import htb


config = config.Config()

htb = htb.HTB()
if config.token:
    htb.set_token(config.token)
else:
    htb.get_token(config.email, config.password)

machines = htb.get_retired_machines()
with open(f"{config.data_path}/machines_retired.json", "w") as f:
    json.dump(machines, f, indent=4)
