import os
import locale
import json
import threading

from utils import get_config
from constants import (
    ENCODING,
    FILE_NAME_GREETINGS,
    DEFAULT_GREETING_FIRST,
    SEP,
    DEFAULT_GREETING_SECOND,
    EMOJI_ENCODINGS,
    WORLD_EMOJI,
    GREETING_PUNCTUATION
)
from translator.factory import get_translator_instance

def read_greetings_file(file_name):
    """Read greetings from a file."""
    try:
        with open(file_name, 'r', encoding = ENCODING ) as file_greeting:
            return file_greeting.readlines()
    except FileNotFoundError:
        print(f"file '{file_name}' does not exist.")
        return None
    except OSError as e:
        print(f"Error: {e}")


def get_greeting(current_locale):
    """Find the matching greeting based on language code."""
    #thread_id = threading.current_thread().ident
    #print(f"Function get_greeting executed on thread with ID: {thread_id}")
    config = get_config()
    translator = get_translator_instance(config)

    language_code = current_locale[0]

    lines = read_greetings_file(FILE_NAME_GREETINGS)

    language_found = False

    for line in lines:
        lang_code, greeting = line.strip().split(':')
        if language_code.startswith(lang_code):
            return greeting
        else:
            continue

    if not language_found:
        print(f"no greeting found for the locale language '{language_code}'; retrieving the translation")
        lang = language_code[:2]
        greeting = translator.get_translation(DEFAULT_GREETING_FIRST + SEP + DEFAULT_GREETING_SECOND , lang)
        if greeting.strip():
            #save retrieved translation in the local file
            save_greeting_background(lang, greeting)
            return greeting
        else:
            print(f"translation could not be retrieved for the locale language '{language_code}'; using default English")
            return (DEFAULT_GREETING_FIRST + SEP + DEFAULT_GREETING_SECOND)


def save_greeting_background(language_code, greeting_text):
    """call save_greeting function in a separate thread allowing the program to continue its execution
    without waiting for the file-writing operation to complete."""
    thread = threading.Thread(target=save_greeting, args=(language_code, greeting_text))
    thread.start()


def save_greeting(language_code, greeting_text):
    """Save greetings in a local file."""
    #thread_id = threading.current_thread().ident
    #print(f"Function save_greeting executed on thread with ID: {thread_id}")
    try:
        data_to_save = f"{language_code}:{greeting_text}"

        with open(FILE_NAME_GREETINGS, 'a', encoding=ENCODING) as file_greeting:
            file_greeting.write("\n")
            file_greeting.write(data_to_save)

        print(f"data appended to {FILE_NAME_GREETINGS}")
    except OSError as e:
        print(f"Error: {e}")


def get_end_greeting():

    current_locale = locale.getlocale()
    encoding = current_locale[1]

    if encoding in EMOJI_ENCODINGS:
        return WORLD_EMOJI + GREETING_PUNCTUATION
    else:
        return GREETING_PUNCTUATION


def print_greeting(text):
    print(text + SEP + get_end_greeting())
