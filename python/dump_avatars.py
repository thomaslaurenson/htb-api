"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Dump machine avatars from the HTB API and save to the data/ folder in base64 JSON.
"""
import json
import base64
from io import BytesIO

import requests
from PIL import Image

import config
import data


BASE_URL = "https://www.hackthebox.eu"
USER_AGENT = "curl/7.68.0"


def fetch_single_avatar(avatar_url: str) -> str:
    """Dump a HTB machine avatar from provided avatar path.

    :param avatar_url: The URL suffix of the machine avatar:
    :return: A base64 string of the image.
    """
    headers = {
        "User-Agent": USER_AGENT,
    }
    r = requests.get(avatar_url,
                     headers=headers)

    img_data = r.content

    # Open ONG image using Pillow
    im = Image.open(BytesIO(img_data))
    # Resize, as HTB avatars vary in size
    im = im.resize((200, 200))
    # Reduce image quality (big saving on size)
    im = im.quantize(method=2)

    # Dump Image object as bytes
    img_byte_arr = BytesIO()
    im.save(img_byte_arr, format='PNG')

    # Get the bytes, and convert to base64
    img_byte_arr = img_byte_arr.getvalue()
    img_b64 = base64.b64encode(img_byte_arr)
    img_b64_str = img_b64.decode('utf-8')

    return img_b64_str


def dump_htb_avatars():
    """Dumps all machine avatars from HTB."""
    print("[*] Dumping HTB machine avatars...")

    all_machines = data.MACHINES_ALL
    all_machines = sorted(all_machines, key=lambda i: i["id"])

    machines_avatars = data.MACHINES_AVATARS

    for machine in all_machines:
        machine_id = str(machine["id"])

        if machine_id in machines_avatars:
            print(f"[*] Skipping machine ID: {machine_id}")
            continue

        print(f"[*] Processing machine ID: {machine_id}")
        avatar_path = machine["avatar"]
        avatar_url = f"{BASE_URL}{avatar_path}"
        img_b64_str = fetch_single_avatar(avatar_url)
        machines_avatars[machine_id] = img_b64_str

    # Dump image data to JSON file
    with open(f"{config.DATA_PATH}/machines_avatars.json", "w") as f:
        json.dump(machines_avatars, f, indent=4)


if __name__ == '__main__':
    # Dump all machines avatars
    dump_htb_avatars()
