# stability.py

import base64
import requests
import os

from image.interface import ImageInterface
from utils import get_key_image

class StabilityImageService(ImageInterface):
    def __init__(self, config):
        self.api_key = get_key_image(),

    def create(self, country_code, text):
        url = "https://api.stability.ai/v1/generation/stable-diffusion-v1-6/text-to-image"

        body = {
            "steps": 40,
            "width": 512,
            "height": 512,
            "seed": 0,
            "cfg_scale": 5,
            "samples": 1,
            "text_prompts": [
                {
                    "text": f'exact text "{text}" on the image and background related to country with iso code {country_code}',
                    "weight": 1
                },
                {
                    "text": "blurry, bad",
                    "weight": -1
                }
            ],
        }

        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}",
        }

        response = requests.post(url, headers=headers, json=body)

        if response.status_code != 200:
            raise Exception("Non-200 response: " + str(response.text))

        data = response.json()

        # make sure the out directory exists
        if not os.path.exists("./out"):
            os.makedirs("./out")

        for i, image in enumerate(data["artifacts"]):
            with open(f'./out/txt2img_{image["seed"]}.png', "wb") as f:
                f.write(base64.b64decode(image["base64"]))
