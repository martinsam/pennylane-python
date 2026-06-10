import requests


class HttpClient:
    def __init__(self, api_key: str, base_url: str) -> None:
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")

    def get(self, path: str) -> dict:
        response = requests.get(
            f"{self.base_url}{path}",
            headers={"Authorization": f"Bearer {self.api_key}"},
            timeout=30,
        )
        response.raise_for_status()
        return response.json()