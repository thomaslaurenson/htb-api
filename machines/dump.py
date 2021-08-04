"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Dump data from the HTB API and save to the data/ folder for offline processing.
"""
import os
import json

import requests
from dotenv import load_dotenv

import config


load_dotenv()

BASE_URL = "https://www.hackthebox.eu/api/v4"
USER_AGENT = "curl/7.68.0"


def get_htb_login_token() -> str:
    """Login to HTB using normal user account.

    :return token: Returns a token string.
    """
    print("[*] Getting HTB login token...")

    url = f"{BASE_URL}/login"

    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json;charset=utf-8"
    }

    data = {
        "email": os.getenv("EMAIL"),
        "password": os.getenv("PASSWORD"),
        "remember": True
    }

    r = requests.post(url,
                      headers=headers,
                      json=data)

    data = r.json()
    token = data["message"]["access_token"]

    print(f"[*] Token: {token}")

    return token


def dump_htb_endpoint(token: str, endpoint: str, out_file_name: str):
    """Dumps data from a HTB endpoint.

    :param endpoint: String endpoint name.
    :param out_file_name: Name for the output file.
    """
    print(f"[*] Dumping endpoint: {endpoint}")

    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json",
        "Authorization": f"Bearer {token}"
    }

    url = f"https://www.hackthebox.eu/api/v4/{endpoint}"

    r = requests.get(url,
                     headers=headers)

    data = r.json()
    with open(f"{config.DATA_PATH}/{out_file_name}.json", "w") as f:
        json.dump(data, f, indent=4)


if __name__ == '__main__':
    token = get_htb_login_token()

    # Dump active machines
    dump_htb_endpoint(token=token,
                      endpoint="machine/list",
                      out_file_name="machines_active")

    # Dump retired machines
    dump_htb_endpoint(token=token,
                      endpoint="machine/list/retired",
                      out_file_name="machines_retired")

    # Dump starting point machines
    dump_htb_endpoint(token=token,
                      endpoint="sp/machines",
                      out_file_name="machines_startingpoint")
