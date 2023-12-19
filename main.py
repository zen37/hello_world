import sys
import locale

from utils import configure_logging, load_environment_variables, set_locale, get_country_code, get_prompt_image, tokens_count
from text import get_greeting, print_greeting
from audio import talk
from visual import create_image



def init():
    configure_logging()
    load_environment_variables()


def main():
    try:
        init()

        current_locale = locale.getlocale()

        greeting = get_greeting(current_locale)
        print_greeting(greeting)

        language_code = current_locale[0]
        talk(language_code, greeting)

        country_code = get_country_code(language_code)
        prompt_text = get_prompt_image()
        prompt = prompt_text.format(greeting=greeting, country_code=country_code)
        create_image(country_code, prompt)

    except FileNotFoundError as file_error:
        print(f"File not found: {file_error}")
    except (locale.Error, ValueError) as locale_error:
        print(f"Error with locale or value: {locale_error}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) == 2:
        lang = sys.argv[1]
        print("argument: ", lang)
        set_locale(lang, 'UTF-8')

    print("current locale:", locale.getlocale())
    main()