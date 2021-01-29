# Sai Raghavendra Aditya
# Notes:
# 1. Translate Text to English by default
# 2. User has flexibility to convert to any of language ( simply set dest_lang=<> while creating object )
# 3. If  user entered language is not found in LANGUAGES list then using TextBlob extract the language using text
# 4.

from textblob import TextBlob
from google_trans_new import google_translator,LANGUAGES

class Translate:
    """Translate Class accepts audio/text as input and translates to English"""
    def __init__(self, src_lang, dest_lang='en'):
        print("Translate:__init__()")
        self.translator    = google_translator()
        self.src_language  = src_lang
        self.dest_language = dest_lang

    def convert_to_english(self,user_text):
        if self.src_language.lower() in LANGUAGES:
            self.translated_text = self.translator.translate(user_text, lang_src=self.src_language, lang_tgt=self.dest_language)
            return(self.translated_text)
        else:
            self.detected_lang = LANGUAGES[TextBlob(user_text).detect_language()]
            self.translated_text = self.translator.translate(user_text, lang_src=self.detected_lang, lang_tgt=self.dest_language)
            return(self.translated_text)