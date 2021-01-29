# Sai Raghavendra Aditya
# Notes:
# 1. Accept User Language voice -> Text
# 2. Remove Stop words like (aaa, blah ) from text
# 3.


import traceback
import speech_recognition as sr
from translate_eng import Translate


class SpeechToText:
    """SpeechToText Class accepts audio/speech as input and translates that to text"""
    def __init__(self,language):
        print("SpeechToText:__init__()")
        self.recognizer     = sr.Recognizer()
        self.user_language  = language
        self.translate      = Translate(self.user_language)

    def microphone_audio_to_text(self):
        try:
            with sr.Microphone() as mp:
                print("Speak...")
                self.recognizer.adjust_for_ambient_noise(mp)
                self.audio = self.recognizer.listen(mp)
                self.save_audio_file()
                self.text = self.recognizer.recognize_google(self.audio, language=self.user_language).lower()
                self.trans_lang_text = self.translate.convert_to_english(self.text)
                print(f"{self.text} => {self.trans_lang_text}")
        except:
            pass

    def audio_file_to_text(self,audio_file):
        try:
            with sr.AudioFile(audio_file) as source:
                self.recognizer.adjust_for_ambient_noise(source)
                self.audio_wav = self.recognizer.listen(source)
                self.audio_text = self.recognizer.recognize_google(self.audio_wav, language=self.user_language).lower()
                self.trans_audio_text = self.translate.convert_to_english(self.audio_text)
                print(f"{self.text} => {self.trans_audio_text}")
        except:
            pass

    def save_audio_file(self):
        with open("recorded.wav","wb") as f:
            f.write(self.audio.get_wav_data())

