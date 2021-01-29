# Sai Raghavendra Aditya
# Notes:
# 1. User choice through command line ( Speech-Text or Text-Speech )
# 2. Provide as a REST API ( flask )
# 3. use google cloud api & capture results
# 4. compare confidence interval b/w api & package results and provide the best
# 5. Apply NLP
# 6. Train verizon Domain Specific Keywords
# 7. Spacy + Vocab
# 8.

import os
import sys
import traceback
import datetime
import signal
import time
from text_to_speech import TextToSpeech
from speech_to_text import SpeechToText

if __name__ == '__main__':

    try:
        print("Welcome to Speech Translation Bot")
        print("1. Speech To Text")
        print("2. Text to Speech")

        usr_input     = int(input("Enter your choice:   "))
        if usr_input in [1, 2]:
            usr_pref_lang = input("Enter your preferred Language:   ")
            print("%s %s"%("Speech To Text" if usr_input ==1 else "Text to Speech",usr_pref_lang))

        if usr_input == 1:
            stt_obj = SpeechToText(usr_pref_lang)
            while True:
                stt_obj.microphone_audio_to_text()
        elif usr_input == 2:
            tts_obj = TextToSpeech(usr_pref_lang)
            while True:
                tts_obj.translate_user_text()
        else :
            print("Invalid Option")
    except:
        #print(traceback.format_exc())
        pass
