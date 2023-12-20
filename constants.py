#common
SERVICE_AZURE = "azure"
SERVICE_STABILITY = "stability"

TRANSLATION_SERVICE = "translation_service"
SPEECH_SERVICE      = "speech_service"
IMAGE_SERVICE       = "image_service"

SERVICES = [TRANSLATION_SERVICE, SPEECH_SERVICE, IMAGE_SERVICE]

SERVICE_KEY_MAPPING = {
    TRANSLATION_SERVICE: "API_KEY_TRANSLATOR",
    SPEECH_SERVICE: "API_KEY_SPEECH",
    IMAGE_SERVICE: "API_KEY_IMAGE",
}

DIR_CONFIG = "config"
FILE_COMMON_CONFIG = "_config.json"
FILE_AZURE_CONFIG = "azure.json"

FORMAT_TIME = "%Y%m%d%H%M%S"

#text
FILE_NAME_GREETINGS = 'files/greetings.txt'
FILE_PROMPT_IMAGE = 'files/prompt_image.txt'

DEFAULT_GREETING_FIRST = 'Hello'
DEFAULT_GREETING_SECOND = 'World'
SEP =  ' '

GREETING = DEFAULT_GREETING_FIRST  + SEP + DEFAULT_GREETING_SECOND

WORLD_EMOJI = '🌍'
GREETING_PUNCTUATION = '!'

EMOJI_ENCODINGS = ('UTF-8', 'UTF-16', 'UTF-32')

ENCODING = 'UTF-8'

TIMEOUT_SECONDS = 10 #for calling translator resource

#speech
DIR_AUDIO ='files/audio'
DEFAULT_VOICE = 'en-US-JennyMultilingualNeural.wav'

#images
DIR_IMAGES = 'files/images'
FILE_IMAGE_EXT  = 'png'


# supported values are “1792x1024”, “1024x1024” and “1024x1792”
DEFAULT_IMAGE_SIZE = '1024x1024'
# options are “hd” and “standard”; defaults to standard
DEFAULT_IMAGE_QUALITY = 'standard'
# options are “natural” and “vivid”; defaults to “vivid”
DEFAULT_IMAGE_STYLE = 'natural'