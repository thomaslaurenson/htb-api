import base64
from io import BytesIO

import requests
from PIL import Image


class HTB:
    """Class for HTB related functions"""
    def __init__(self):
        self.base_url = "https://www.hackthebox.eu/api/v4"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/120.0"
        }
        self.token: None

    def get_token(self, email: str, password: str) -> str:
        """Get HTB token using normal user account.

        :return token: Returns a token string.
        """
        url = f"{self.base_url}/login"

        headers = self.headers
        headers["Content-Type"] = "application/json;charset=utf-8"

        data = {
            "email": email,
            "password": password,
            "remember": True
        }

        r = requests.post(url,
                          headers=headers,
                          json=data)

        data = r.json()
        token = data["message"]["access_token"]

        print(f"[*] HTB token set: {token}")
        self.token = token
        return token

    def set_token(self, token: str) -> bool:
        """Set HTB token.

        :return token: Returns a success.
        """
        print("[*] Using existing token...")
        self.token = token
        return True

    def get_active_machines(self) -> list:
        """Fetch all active machines from HTB."""
        return self._get_endpoint("machine/paginated")

    def get_retired_machines(self) -> list:
        """Fetch all retired machines from HTB."""
        return self._get_endpoint("machine/list/retired/paginated")

    def _get_endpoint(self, endpoint: str) -> list:
        """Dumps data from a HTB endpoint.

        :param endpoint: String endpoint name.
        :return data: JSON data repsponse.
        """
        machines_list = list()

        headers = self.headers
        headers["Content-Type"] = "application/json;charset=utf-8"
        headers["Authorization"] = f"Bearer {self.token}"

        params = {
            "page": 1,
            "per_page": 100,
        }

        url = f"{self.base_url}/{endpoint}"

        print(f"[*] Fetching page: {params['page']}")
        r = requests.get(url,
                         params=params,
                         headers=headers)

        data = r.json()
        machines_list += data["data"]
        last_page = data["meta"]["last_page"]

        while params["page"] <= last_page:
            params["page"] = params["page"] + 1
            print(f"[*] Fetching page: {params['page']}")

            r = requests.get(url,
                             params=params,
                             headers=headers)
            data = r.json()
            machines_list += data["data"]

        return machines_list

    def get_avatar(self, avatar_url: str) -> str:
        """Dump a HTB machine avatar from provided avatar path.

        :param avatar_url: The URL suffix of the machine avatar:
        :return: A base64 string of the image.
        """
        url = f"https://hackthebox.com{avatar_url}"

        r = requests.get(url,
                         headers=self.headers)

        if r.status_code != 200:
            return None

        img_data = r.content

        # Open PNG image using Pillow
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
