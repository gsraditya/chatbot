# Sai Raghavendra Aditya
# Notes:
# 1. Accept user specific language text and convert to english
# 2. Remove Stop words
# 3. english text -> voice

import pyttsx3
import traceback
from textblob import TextBlob
from google_trans_new import google_translator,LANGUAGES
from translate_eng import Translate


class TextToSpeech:
    """TextToSpeech Class accepts text as input and translates that to speech"""
    def __init__(self,language):
        print("TextToSpeech:__init__()")
        self.user_language  = language
        self.translate      = Translate(self.user_language)
        self.engine         = pyttsx3.init()
        self.voices         = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[1].id)

    def translate_user_text(self):
        try:
            print("Type...")
            self.text = input()
            self.trans_lang_text = self.translate.convert_to_english(self.text)
            print(f"{self.text} => {self.trans_lang_text}")
            self.text_to_audio(self.trans_lang_text)
        except:
            pass

    def text_to_audio(self,text_message):
        self.engine.say(text_message)
        self.engine.runAndWait()


