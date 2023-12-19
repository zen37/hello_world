# factory.py

from utils import get_config_service


def get_speech_instance(config):

    service = config.get("speech_service", "").lower()
    config_service = get_config_service(service)

    if service == "azure":
        from speech.services.azure import AzureSpeechService
        return AzureSpeechService(config_service)
    #elif translation_service == "openai":
    #    from translator_openai import OpenAITranslator
    #    return OpenAITranslator(config)
    else:
        raise ValueError("Invalid speech service specified in the config.")

