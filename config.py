"""
Author: Thomas Laurenson
Email: thomas@thomaslaurenson.com
URL: https://github.com/thomaslaurenson/htp-api
Description: Project config.
"""
from pathlib import Path

PROJECT_ROOT_PATH = Path(__file__).parent

DATA_PATH = Path(PROJECT_ROOT_PATH / "data")
DATA_AVATARS_PATH = Path(PROJECT_ROOT_PATH / "data" / "avatars")
MACHINES_PATH = Path(PROJECT_ROOT_PATH / "machines")
