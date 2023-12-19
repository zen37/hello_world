# azure_speech.py

import os
import random
import azure.cognitiveservices.speech as speechsdk

from utils import get_config_service, get_key_speech
from constants import DEFAULT_VOICE, DIR_AUDIO
from speech.services.common import get_audio_file, get_filepath, play
from speech.interface import SpeechInterface


class AzureSpeechService(SpeechInterface):
    def __init__(self, config):
        super().__init__()  # Initialize the base class (SpeechInterfac)
        self.config = config  # Use the passed configuration instead of loading from file

    def get_available_voices(self):
        speech_synthesizer = self.get_speech_synthesizer()
        result = speech_synthesizer.get_voices_async().get()
        if result.reason == speechsdk.ResultReason.VoicesListRetrieved:
            print('available voices successfully retrieved')
            return result.voices
        elif result.reason == speechsdk.ResultReason.Canceled:
            print(f"Speech synthesis canceled; error details: {result.error_details}")
            return None

    def get_voice(self, language_code):
        voice_names = []
        voices = self.get_available_voices()
        for voice in voices:
            if (voice.locale[:2] == language_code):
                voice_names.append(voice.short_name)

        if voice_names:
            return random.choice(voice_names)
        else:
            return DEFAULT_VOICE


    def get_speech_config(self, voice=None):

        config = get_config_service("azure")
        REGION = config["region"]
        KEY = get_key_speech()

        speech_config = speechsdk.SpeechConfig(subscription=KEY, region=REGION)
        if voice:
            speech_config.speech_synthesis_voice_name = voice

        return speech_config


    def get_speech_synthesizer(self, voice=None, audio_config=None):
        speech_config = self.get_speech_config(voice)
        if audio_config:
            speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=audio_config)
        else:
            speech_synthesizer = speechsdk.SpeechSynthesizer(speech_config=speech_config, audio_config=None)

        return speech_synthesizer


    def talk(self, language_locale, text):
        language_code = language_locale[:2]
        #voice = self.get_audio_file(language_code)
        voice = get_audio_file(language_code)

        if voice:
            #filepath = self.get_filepath(language_code, voice)
            filepath = get_filepath(language_code, voice)
            play(filepath)
        else:
            voice = self.get_voice(language_code)
            print("voice: ", voice)
            filepath = get_filepath(language_code, voice)
            print("filepath: ", filepath)
            audio_config = speechsdk.audio.AudioOutputConfig(use_default_speaker=True, filename=filepath)
            speech_synthesizer = self.get_speech_synthesizer(voice, audio_config)
            speech_synthesis_result = speech_synthesizer.speak_text_async(text).get()

            if speech_synthesis_result.reason == speechsdk.ResultReason.SynthesizingAudioCompleted:
                print(f"speech synthesized for voice [{voice}] and text [{text}]")
                filepath = get_filepath(language_code, voice)
                if os.path.isfile(filepath):
                    play(filepath)
            elif speech_synthesis_result.reason == speechsdk.ResultReason.Canceled:
                cancellation_details = speech_synthesis_result.cancellation_details
                print(f"Speech synthesis canceled: [{cancellation_details.reason}]")
                if cancellation_details.reason == speechsdk.CancellationReason.Error:
                    if cancellation_details.error_details:
                        print(f"Speech synthesized for text [{cancellation_details.error_details}]")
                        print("Did you set the speech resource key and region values?")
