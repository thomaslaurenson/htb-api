import json
import os
from pathlib import Path

from dotenv import load_dotenv


load_dotenv()


class Config:
    def __init__(self):
        # Load environment variables
        self.email = os.getenv("EMAIL") or None
        self.password = os.getenv("PASSWORD") or None
        self.token = os.getenv("TOKEN") or None

        # Data structures for storing machine data
        self.machines_active = None
        self.machines_retired = None
        self.machines_avatars = None
        self.machines_oscp_normal = None
        self.machines_oscp_advanced = None

        # Path variables for loading/saving data
        self.project_root_path = Path(__file__).parent.parent
        self.data_path = Path(self.project_root_path / "data")

        self._load_all()

    def _load_all(self):
        fis = [
            "machines_active",
            "machines_retired",
            "machines_avatars",
            "machines_oscp_normal",
            "machines_oscp_advanced",
        ]

        for fi in fis:
            fi_path = Path(self.data_path / f"{fi}.json")

            if not fi_path.is_file():
                print(f"[*] Warning: {fi}.json not found! Some scripts might not work.")

            with open(f"{self.data_path}/{fi}.json") as f:
                data = json.load(f)
                setattr(self, fi, data)
