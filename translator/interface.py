"""
Module: translator_interface.py
Description: Define an abstract base class for translation services.
"""
from abc import ABC, abstractmethod

class TranslatorInterface(ABC):
    """An abstract base class for translation services."""
    @abstractmethod
    def get_translation(self, text, language):
        """
        Translate the given text to the specified language.

        Parameters:
        - text (str): The text to be translated.
        - language (str): The target language for translation.

        Returns:
        - str: The translated text.
        """