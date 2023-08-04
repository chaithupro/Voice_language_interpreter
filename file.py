# import required modules

import pygame
from playsound import playsound
import speech_recognition as sr
from googletrans import Translator
from gtts import gTTS
import os
import pygame

# Global variables
# create of tuple of all languages

dic = ('afrikaans', 'af', 'albanian', 'sq', 'amharic', 'am', 'arabic', 'ar', 'armenian', 'hy', 'azerbaijani', 'az',
       'basque', 'eu', 'belarusian', 'be', 'bengali', 'bn', 'bosnian',
       'bs', 'bulgarian', 'bg', 'catalan', 'ca',
       'cebuano', 'ceb', 'chichewa', 'ny', 'chinese (simplified)',
       'zh-cn', 'chinese (traditional)', 'zh-tw',
       'corsican', 'co', 'croatian', 'hr', 'czech', 'cs', 'danish',
       'da', 'dutch', 'nl', 'english', 'en', 'esperanto',
       'eo', 'estonian', 'et', 'filipino', 'tl', 'finnish', 'fi',
       'french', 'fr', 'frisian', 'fy', 'galician', 'gl',
       'georgian', 'ka', 'german', 'de', 'greek', 'el', 'gujarati',
       'gu', 'haitian creole', 'ht', 'hausa', 'ha',
       'hawaiian', 'haw', 'hebrew', 'he', 'hindi', 'hi', 'hmong',
       'hmn', 'hungarian', 'hu', 'icelandic', 'is', 'igbo',
       'ig', 'indonesian', 'id', 'irish', 'ga', 'italian', 'it',
       'japanese', 'ja', 'javanese', 'jw', 'kannada', 'kn',
       'kazakh', 'kk', 'khmer', 'km', 'korean', 'ko', 'kurdish (kurmanji)',
       'ku', 'kyrgyz', 'ky', 'lao', 'lo',
       'latin', 'la', 'latvian', 'lv', 'lithuanian', 'lt', 'luxembourgish',
       'lb', 'macedonian', 'mk', 'malagasy', 'mg', 'malay', 'ms', 'malayalam', 'ml', 'maltese', 'mt', 'maori',
       'mi', 'marathi', 'mr', 'mongolian', 'mn',
       'myanmar (burmese)', 'my', 'nepali', 'ne', 'norwegian', 'no',
       'odia', 'or', 'pashto', 'ps', 'persian',
       'fa', 'polish', 'pl', 'portuguese', 'pt', 'punjabi', 'pa',
       'romanian', 'ro', 'russian', 'ru', 'samoan',
       'sm', 'scots gaelic', 'gd', 'serbian', 'sr', 'sesotho',
       'st', 'shona', 'sn', 'sindhi', 'sd', 'sinhala',
       'si', 'slovak', 'sk', 'slovenian', 'sl', 'somali', 'so',
       'spanish', 'es', 'sundanese', 'su',
       'swahili', 'sw', 'swedish', 'sv', 'tajik', 'tg', 'tamil',
       'ta', 'telugu', 'te', 'thai', 'th', 'turkish', 'tr',
       'ukrainian', 'uk', 'urdu', 'ur', 'uyghur', 'ug', 'uzbek',
       'uz', 'vietnamese', 'vi', 'welsh', 'cy', 'xhosa', 'xh',
       'yiddish', 'yi', 'yoruba', 'yo', 'zulu', 'zu')


# Voice Commands

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        q = r.recognize_google(audio, language='en-in')
        print(f"User said:  {q}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    return q


# Take Voice Inputs

q = takecommand()
while (q == "None"):
    q = takecommand()

# Input Destination language from the user


def destination_language():
    lang = input("Enter the language in which you want to convert:")
    print()
    return lang.strip()


to_lang = destination_language()

# print(to_lang)

while (to_lang not in dic):
    print(
        "Language in which you are trying to convert is currently not available, please input some other language")
    to_lang = destination_language()
    print()


# to_lang = dic[dic.index(to_lang) + 1]

# Calling Translator

translator = Translator()

# Translating from src to dest
translatedText = translator.translate(q, dest=to_lang)
text = translatedText.text

# Saving first and then deleting translating files

speak = gTTS(text=text, lang=to_lang, slow=False)
speak.save("captured_voice.mp3")

# playsound("C:\Users\MUNNA\Downloads\Projects SDE\Voice_language_intrepretar\.vscode")


def play_audio(file_path):
    pygame.mixer.init()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pass


if __name__ == "__main__":
    mp3_file = "captured_voice.mp3"  # Replace this with the path to your MP3 file
    play_audio(mp3_file)
