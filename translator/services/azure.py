"""
Module: translator_azure.py
Description: Provides functions for translating text using Azure Translator service.
"""

import uuid
import json
import requests

from utils import get_key_translation
from constants import TIMEOUT_SECONDS
from translator.interface import TranslatorInterface

class AzureTranslator(TranslatorInterface):
    """
    AzureTranslator class for translating text using the Azure Translator service.

    Attributes:
    - config (dict): Configuration settings for the Azure Translator.

    Methods:
    - __init__(self, config): Constructor method for initializing the AzureTranslator.
    - get_translation(self, text, language): Translate the given text to the specified language.
    """
    def __init__(self, config):
        super().__init__()  # Initialize the base class (TranslatorInterface)
        self.config = config  # Use the passed configuration instead of loading from file

    def get_translation(self, text, language):
        """Translate the given text to the specified language."""
        params = {
            'api-version': self.config["api_version_translator"],
            'from': self.config["translate_from"],
            'to': [language]
        }

        trace_id = f'{str(uuid.uuid4())}'
        headers = {
            #'Ocp-Apim-Subscription-Key': self.config["key_translator"],
            'Ocp-Apim-Subscription-Key': get_key_translation(),
            'Ocp-Apim-Subscription-Region': self.config["region"],
            'Content-type': 'application/json',
            'X-ClientTraceId': trace_id
        }

        body = [{'text': text}]

        url = self.config["endpoint_translator"]
        timeout = TIMEOUT_SECONDS

        try:
            request = requests.post(url, params=params, headers=headers, json=body, timeout=timeout)
            request.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)

            # Process the response
            response = request.json()
            translation_text = response[0]['translations'][0]['text']

            return translation_text

        except requests.exceptions.HTTPError as http_err:
            # Handle HTTP errors (4xx and 5xx)
            raise TranslationError(f"HTTP error occurred: {http_err}") from http_err
        except requests.exceptions.Timeout as req_err:
            raise TranslationError(f"Request timed out.: {req_err}") from req_err
        except requests.exceptions.RequestException as req_err:
            # Handle other request-related errors
            raise TranslationError(f"Request error occurred: {req_err}") from req_err
        except json.JSONDecodeError as json_err:
            # Handle JSON decoding errors
            raise TranslationError(f"JSON decoding error occurred: {json_err}") from json_err
        except KeyError as key_err:
            # Handle key errors in the response structure
            raise TranslationError(f"Key error occurred: {key_err}") from key_err
        except Exception as e:
            # Handle other unexpected errors
            raise TranslationError(f"An unexpected error occurred: {e}") from e

# Custom exception for translation errors
class TranslationError(Exception):
    """Custom exception for translation errors."""
