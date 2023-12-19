from utils import get_config
from image.factory import get_image_instance


def create_image(country_code, text):

    config = get_config()
    image = get_image_instance(config)
    image.create(country_code, text)