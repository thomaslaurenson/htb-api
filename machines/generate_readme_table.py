"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Generate the tables for my trophy_room project README file.
"""
from datetime import datetime

import data


HTB_BADGE_ICON = ("iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9TpSoVBTuIOG"
                  "SonSyIFXHUKhShQqgVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi5uak6CIl/q8ptIjx4Lgf7+497t4BQr3MNKtrAtB0"
                  "20wl4mImuyoGXtGLQQwhgpjMLGNOkpLwHF/38PH1LsqzvM/9OfrVnMUAn0g8ywzTJt4gnt60Dc77xCFWlFXic+Jxky5I/Mh1xe"
                  "U3zoUmCzwzZKZT88QhYrHQwUoHs6KpEU8Rh1VNp3wh47LKeYuzVq6y1j35C4M5fWWZ6zRHkcAiliBBhIIqSijDRpRWnRQLKdqP"
                  "e/hHmn6JXAq5SmDkWEAFGuSmH/wPfndr5WOTblIwDnS/OM7HGBDYBRo1x/k+dpzGCeB/Bq70tr9SB2Y+Sa+1tfARMLANXFy3NW"
                  "UPuNwBhp8M2ZSbkp+mkM8D72f0TVlg6BboW3N7a+3j9AFIU1fJG+DgEIgUKHvd4909nb39e6bV3w+413LD6ZqKlQAAAAZiS0dE"
                  "ABQAHQAr1GFDXgAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+UJEBMoBwoNM18AAAAZdEVYdENvbW1lbnQAQ3JlYXRlZC"
                  "B3aXRoIEdJTVBXgQ4XAAACAUlEQVQoz4WST0iTYRzHv8/j2/7l/gRDFuIkEkSQmL7VCgxiHix2GBEsJnTolgc7KHgpiKAugR66"
                  "zJuHgVtiyKCgSxEtaO9qortIhzHYEERS33eu951tPr8OYzKn0vf2PHy+z/P782U4RUvabV+V8rMAYGGXp8POL2vtDG89JMvBrp"
                  "jaF9VFWuEwFThMBV2klZjaF02Wg12tLAOAT5VHpq16eqJOW88Zc+QsrGcq7Py22vh9ZLhKpTki7YrELr7wSDeio50Lf1lCle0H"
                  "VFAE9votbHg84sq+Pa38uCo/qNLqIseFX2Z2yc8NyroEdgcA4jVsP06ostxuSqiyXMP2BEBcYHfAoKzrqEcrv34XAAxaz8TU3v"
                  "llLeBZ1gKemNo7b9B6BgA1mWPDMUQm5bdNBsxsMCJIH6sIZaMilA1B+piZDUb8tsmAITKpJi+1ltRvmiEAS8nyvffq4dcPAODq"
                  "GAmGHCs6sIaFvTPW0VTIsaIL7JQEdkoN00kdGTv5qBn/USvDrXxI43DndZFLx1Vf6CxTXPWFdJFLc7jzVj6kMQD4uP/Q+vvwx5"
                  "M6bT7lzP7dzHqmdfFzBgBs/OrrAyrNCtq/KbHuV+6Oa2/u2GMGa331XTnQbYjiyzoVx4Hztcbtn3MS8y5auffZfcfnzWOROxny"
                  "W/4qFecaIfdOhZ0ppZ35B+U31U10XP4mAAAAAElFTkSuQmCC")

HTB_OSCP_NORMAL_COMPLETED = 0
HTB_COMPLETED = 0
HTB_SP_COMPLETED = 0

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
}

PUBLISHED_DATE_LOOKUP_SP = {
    "Archetype": "2021-07-08",
    "Oopsie": "2021-07-10",
    "Vaccine": "2021-07-11",
    "Shield": "2021-07-29",
}


# Make machine lookup dict
machines_retired_lookup = dict()
for machine in data.MACHINES_RETIRED:
    machines_retired_lookup[machine["name"].lower()] = machine
machines_startingpoint_lookup = dict()
for machine in data.MACHINES_STARTINGPOINT:
    machines_startingpoint_lookup[machine["name"].lower()] = machine

machines_completed = [machine_name.lower() for machine_name in PUBLISHED_DATE_LOOKUP.keys()]
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
        # Count completed OSCP-like boxes for custom badge
        HTB_OSCP_NORMAL_COMPLETED += 1
    elif name in data.MACHINES_OSCP_ADVANCED:
        trophy_list = "Yes (advanced)"
    else:
        trophy_list = "No"

    # Count a finished box
    HTB_COMPLETED += 1

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} | {release} | {published} |")

machines_completed = [machine_name.lower() for machine_name in PUBLISHED_DATE_LOOKUP_SP.keys()]

# Starting Point: Generate a nice table for the README file
print("| Name | System | Difficulty | Trophy List | Release Date | Published Date |")
print("| ---- |--------|------------|-------------|--------------|----------------|")
for i, machine_name in enumerate(machines_completed):
    machine_data = machines_startingpoint_lookup[machine_name]
    name = machine_data["name"]
    url = f"hackthebox/startingpoint/{i + 1}_{machine_name}"
    os = machine_data["os"]
    difficulty = machine_data["difficultyText"]
    release = datetime.strptime(machine_data["release"], "%Y-%m-%dT%H:%M:%S.%fZ")
    release = release.strftime("%Y-%m-%d")
    published = PUBLISHED_DATE_LOOKUP_SP[name]
    trophy_list = "No"

    HTB_SP_COMPLETED += 1

    print(f"| [{name}]({url}) | {os} | {difficulty} | {trophy_list} | {release} | {published} |")

# Make a custom HTB badges
base_url = "https://img.shields.io/badge/"

# Make writeup count badge
completed = HTB_COMPLETED + HTB_SP_COMPLETED
badge_str = f"htb%20writeups-{completed}-green&style=plastic?logo=data:image/png;base64,"
badge_url = f"{base_url}{badge_str}{HTB_BADGE_ICON}"
badge = f"![htb writeups]({badge_url})"
print(badge, end=" ")

# Make oscp-like completed percentage badge
oscp_normal_count = len(data.MACHINES_OSCP_NORMAL)
coverage = round(HTB_OSCP_NORMAL_COMPLETED / oscp_normal_count * 100)
badge_str = f"htb%20oscp%20coverage-{coverage}%25-green&style=plastic?logo=data:image/png;base64,"
badge_url = f"{base_url}{badge_str}{HTB_BADGE_ICON}"
badge = f"![htb oscp coverage]({badge_url})"
print(badge)
