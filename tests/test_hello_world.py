import sys
sys.path.append(".")

import locale

from utils import set_locale
from text import get_greeting, read_greetings_file, print_greeting
from constants import FILE_NAME_GREETINGS, SEP, WORLD_EMOJI, ENCODING

def test_get_greeting():
    lines = read_greetings_file(FILE_NAME_GREETINGS)
    assert lines is not None

    greeting = get_greeting(['en_US', ENCODING])
    assert greeting == 'Hello World'

    greeting = get_greeting(['es_ES', ENCODING])
    assert greeting == '¡Hola mundo'

    #greeting = get_greeting(['ro_MD', ENCODING])
    #assert greeting == None


def test_print_greeting(capfd):

    current_locale = locale.getlocale()
    text = get_greeting(current_locale)
    print_greeting(text)

    captured = capfd.readouterr()
    # Print the captured output for inspection (optional, for debugging)
    print("Captured Output:", captured.out)

    greeting =  get_greeting(current_locale)
    print(greeting)
    assert greeting + SEP + WORLD_EMOJI in captured.out


def test_print_greeting_other_lang(capfd):

    langs = ["fr_FR", "de_DE", "it_IT", "ja_JP"]
    captured_outputs = []  # List to store captured outputs

    for lang in langs:
        print(f"Captured Output for {lang}:")
        set_locale(lang, 'UTF-8')
        current_locale = locale.getlocale()
        text = get_greeting(current_locale)
        print_greeting(text)

        captured = capfd.readouterr()
        # Print the captured output for inspection (optional, for debugging)
        print(captured.out)

        # Store the captured output in the list
        captured_outputs.append(captured.out)

        greeting =  get_greeting(current_locale)

        assert greeting + SEP + WORLD_EMOJI in captured.out