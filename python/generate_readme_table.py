from datetime import datetime

import data


HTB_BADGE_ICON = (
    "iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAf"
    "SC3RAAAABmJLR0QA/wD/AP+gvaeTAAABzklEQVQo"
    "z41SPWgTYRh+vu8uLTbkeqiolyFkaRoKEUpKKYWC"
    "ONRmiMUihda0i6ODoFApzg4KCg5udWkMXEUUdGiz"
    "SLp1qKUYh6NZSksJgrH3XZo76CXf6yDVpGnQZ3p5"
    "3+f9f4AOMEVy2BTJ4U5xdtrx3kkZNWk9k/TjJgBw"
    "dvFjkMcXprTVcjOPnxhrR3PdOXtg0WlsWAD3NWW0"
    "X1NG+wHuO40NK2cPLK4dzXW3dMzZfdfr9PM1EPh+"
    "jsfvTfcWvjRXfyuuJT1pvQL8yyo7f/eOXvrMAeCY"
    "ShmJShQgAXjV9o28KkBCohI9plIGANS/MxtLjKmX"
    "XLn1LWtHXgbZ1ScAUKOvj125dZ+zK6ucjCWJstKy"
    "o0R5e17fn+xi8bQkL+XIdcuR65YkL9XF4ul5fX9S"
    "orzddpwTzOrFvKFODALKJqBsGurE4KxezJ/m8bN+"
    "NB7K+gT7gGAfjIey/lmcP4kKwlH8A80cDgABFlsh"
    "uDPLh+GCKYYS7SoaSiwfhgsEdybAYistyvlUvdUj"
    "GsVHdao8UJj2RpIb+a2cnr0GORmVXXjRqySepkMf"
    "3A6SuxGpyZ3nddq9DQAqi74L8tjDKS2/h/+BKUbG"
    "TDEy1in+CwRytDFQHtyiAAAAAElFTkSuQmCC"
)

HTB_OSCP_NORMAL_COMPLETED = 0
HTB_COMPLETED = 0

PUBLISHED_DATE_LOOKUP = {
    "Bashed": "2021-06-27",
    "Shocker": "2021-06-27",
    "Lame": "2021-06-27",
    "Nibbles": "2021-07-03",
    "Beep": "2021-07-03",
    "Cronos": "2021-07-04",
    "Nineveh": "2021-07-06",
    "Sense": "2021-07-16",
    "Spectra": "2021-07-21",
    "Legacy": "2021-07-25",
    "Devel": "2021-07-25",
    "Popcorn": "2021-07-26",
    "Armageddon": "2021-07-26",
    "TheNotebook": "2021-07-03",
    "Writeup": "2021-08-04",
    "OpenAdmin": "2021-08-05",
    "Love": "2021-08-14",
    "Tabby": "2021-08-18",
    "Ophiuchi": "2021-08-19",
    "Jerry": "2021-08-20",
    "Knife": "2021-08-30",
    "Blocky": "2021-09-04",
    "Delivery": "2021-09-05",
    "Postman": "2021-09-04",
    "SwagShop": "2021-09-13",
    "Schooled": "2021-09-15",
    "Valentine": "2021-09-17",
    "Irked": "2021-09-20",
    "Blunder": "2021-09-21",
    "Admirer": "2021-09-22",
    "Networked": "2021-09-26",
    "Doctor": "2021-09-28",
    "FriendZone": "2021-09-30",
    "Blue": "2021-10-04",
    "Paper": "2023-10-30",
}


# Make machine lookup dict
machines_retired_lookup = dict()
for machine in data.MACHINES_RETIRED:
    machines_retired_lookup[machine["name"].lower()] = machine

machines_completed = [machine_name.lower() for machine_name in PUBLISHED_DATE_LOOKUP.keys()]
machines_completed.sort()

# Machines: Generate a nice table for the README file
print("| Name | System | Difficulty | Trophy List | Release Date | Published Date |")
print("| ---- |--------|------------|-------------|--------------|----------------|")
for machine_name in machines_completed:
    machine_data = machines_retired_lookup[machine_name]
    name = machine_data["name"]
    url = f"hackthebox/{machine_name}"
    os = machine_data["os"]
    difficulty = machine_data["difficultyText"]
    release = datetime.strptime(machine_data["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    published = PUBLISHED_DATE_LOOKUP[name]

    if name in data.MACHINES_OSCP_NORMAL:
        trophy_list = "Yes"
        # Count completed OSCP-like boxes for custom badge
        HTB_OSCP_NORMAL_COMPLETED += 1
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    # Count a finished box
    HTB_COMPLETED += 1

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} | {release} | {published} |")

# Make a custom HTB badges
base_url = "https://img.shields.io/badge/"

# Make writeup count badge
completed = HTB_COMPLETED
badge_str = f"htb_writeups-{completed}-green?logo=data:image/png;base64,"
badge_url = f"{base_url}{badge_str}{HTB_BADGE_ICON}"
badge = f"![htb writeups]({badge_url})"
print(badge, end=" ")

# Make oscp-like completed percentage badge
oscp_normal_count = len(data.MACHINES_OSCP_NORMAL)
coverage = round(HTB_OSCP_NORMAL_COMPLETED / oscp_normal_count * 100)
badge_str = f"htb_oscp_coverage-{coverage}%25-green?logo=data:image/png;base64,"
badge_url = f"{base_url}{badge_str}{HTB_BADGE_ICON}"
badge = f"![htb oscp coverage]({badge_url})"
print(badge)
