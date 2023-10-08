import base64
from io import BytesIO
from pathlib import Path

from PIL import Image

import config
import data


def convert_htb_avatars():
    """Convert all machine avatars from HTB to PNGs."""
    print("[*] Converting HTB machine avatars...")

    Path(config.DATA_AVATARS_PATH).mkdir(exist_ok=True)

    for machine_id, img_b64_str in data.MACHINES_AVATARS.items():
        img_data = base64.b64decode(img_b64_str)
        im = Image.open(BytesIO(img_data))
        im_resized = im.resize((300, 300))
        im_filename = f"{config.DATA_AVATARS_PATH}/{machine_id}.png"
        im_resized.save(im_filename)


if __name__ == '__main__':
    # Convert all machines avatars
    convert_htb_avatars()
