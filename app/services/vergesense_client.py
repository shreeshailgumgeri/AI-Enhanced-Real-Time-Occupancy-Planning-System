import requests
import os

class VergeSenseClient:
    def __init__(self):
        self.api_key = os.getenv("VERGESENSE_API_KEY")
        self.api_url = os.getenv("VERGESENSE_API_URL")

    def get_occupancy_data(self, area_id):
        url = f"{self.api_url}/occupancy/{area_id}"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()

    def get_all_areas(self):
        url = f"{self.api_url}/areas"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            return response.json()
        else:
            response.raise_for_status()