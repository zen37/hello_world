import os
import random
# https://stackoverflow.com/questions/51464455/how-to-disable-welcome-message-when-importing-pygame
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from constants import DIR_AUDIO


def get_audio_file(language_code):
    if not os.path.exists(DIR_AUDIO):
        os.makedirs(DIR_AUDIO)
        return None
    else:
        path = os.path.join(DIR_AUDIO, language_code)
        if not os.path.exists(path):
            os.makedirs(path)
            return None

        files = [f for f in os.listdir(path) if f.startswith(language_code)]

        print(f"audio files found locally for '{language_code}': {len(files)}")

        for file in files:
            print(file)

        if files:
            random_file = random.choice(files)
            print("randomly chosen voice: ", random_file)
            return random_file
        else:
            return None


def get_filepath(language_code, filename):
    language_folder = os.path.join(DIR_AUDIO, language_code)
    os.makedirs(language_folder, exist_ok=True)
    filepath = os.path.join(language_folder, filename)

    return filepath


def play(filepath):

    pygame.init()
    pygame.mixer.music.load(filepath)
    pygame.mixer.music.play()
    pygame.time.wait(int(pygame.mixer.Sound(filepath).get_length() * 1000))
    pygame.mixer.quit()
    pygame.quit()
