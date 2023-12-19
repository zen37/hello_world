import locale
import os
import logging
from dotenv import load_dotenv
import json
import inspect
import tiktoken

from constants import ENCODING, DIR_CONFIG, FILE_COMMON_CONFIG, FILE_PROMPT_IMAGE

def set_locale(language, encoding):
    """Set the locale."""
    try:
        locale.setlocale(locale.LC_ALL, f'{language}.{encoding}')
    except Exception as e:
        print(f"Error setting the locale: {e}")
        return None

def log_function_call(func):
    def wrapper(*args, **kwargs):
        caller = inspect.currentframe().f_back.f_code.co_name
        print(f"Function {func.__name__} called by {caller} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

def get_config():
    config_path = os.path.join(DIR_CONFIG, FILE_COMMON_CONFIG)
    with open(config_path, "r", encoding = ENCODING) as file:
        config = json.load(file)
    return config

def get_config_service(provider):
    file_config = provider + ".json"

    config_path = os.path.join(DIR_CONFIG, file_config )

    with open(config_path, "r", encoding = ENCODING) as file:
        config = json.load(file)

    return config

def load_environment_variables():
    config = get_config()

    services = ["translation_service", "speech_service", "image_service"]

    for service_key in services:
        service = config.get(service_key, "").lower()
        secrets_path = os.path.join("env", f"{service}.env")
        load_dotenv(dotenv_path=secrets_path)

def get_key_translation():
    key = os.getenv("KEY_TRANSLATOR")
    return key

def get_key_speech():
    key = os.getenv("KEY_SPEECH")
    return key

def get_key_image():
    key = os.getenv("KEY_IMAGE")
    return key

def get_country_code(language_code):
    components = language_code.split('_')

    # Check if there is a country code
    if len(components) == 2:
        # The country code is the second component
        country_code = components[1]
        return country_code
    else:
        # No valid country code found
        return None

def get_prompt_image():
    with open(FILE_PROMPT_IMAGE, "r") as file:
        prompt_text = file.read()

    return prompt_text

def configure_logging():
    config = get_config()

    logging.basicConfig(
        level=config.get("logging_level", logging.INFO),
        format=config.get("logging_format", "%(asctime)s [%(levelname)s]: %(message)s"),
    )

def tokens_count(model, text):
    enc = tiktoken.encoding_for_model(model)
    print(enc)
    tokens = enc.encode(text)
    print(tokens)