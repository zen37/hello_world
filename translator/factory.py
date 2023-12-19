from utils import get_config_service
from constants import SERVICE_AZURE

def get_translator_instance(config):

    """
    Create an instance of a translation service based on the specified configuration.

    Parameters:
    - config (dict): A dictionary containing configuration parameters.

    Returns:
    - TranslatorInterface: An instance of a translation service implementing the TranslatorInterface.
    """

    service = config.get("translation_service", "").lower()
    config_service = get_config_service(service)

    if service == SERVICE_AZURE:
        from translator.services.azure import AzureTranslator
        return AzureTranslator(config_service)
    #elif translation_service == "openai":
    #    from translator_openai import OpenAITranslator
    #    return OpenAITranslator(config)
    else:
        raise ValueError("Invalid translation service specified in the config.")
