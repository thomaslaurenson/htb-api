"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Project config.
"""
from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parent

DATA_PATH = Path(PROJECT_ROOT_PATH / "data")
MACHINES_PATH = Path(PROJECT_ROOT_PATH / "machines")

TROPHY_ROOM_PATH = Path(PROJECT_ROOT_PATH.parent /
                        "trophy_room" / "hackthebox")
