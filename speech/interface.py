"""
Module: interface.py
Description: Define an abstract base class for speech services.
"""
from abc import ABC, abstractmethod

class SpeechInterface(ABC):
    """An abstract base class for speech services."""
    @abstractmethod
    def talk(self, text, language):
        """
        Translate the given text to the specified language.

        Parameters:
        - text (str): The text to be spoken
        - language (str): The target language for speech

        Returns:
            nothing
        """