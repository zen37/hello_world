from utils import get_config
from speech.factory import get_speech_instance


def talk(language_code, text):

    config = get_config()
    speech = get_speech_instance(config)
    speech.talk(language_code, text)