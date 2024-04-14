# import os
# import time
import pyaudio
# import playsound
# from gtts import gTTS
# import openai
import speech_recognition as sr
import pyttsx3

lang = "en"

# openai.api_key = open("OPENAI_API_KEY.OLD").read()
# openai.api_key = open("OPENAI_API_KEY").read()

ai_name = "dude"

mic = sr.Microphone(device_index=1)
r = sr.Recognizer()
tts = pyttsx3.init()


def listen(mic):
    text = ""
    with mic as source:
        print("Listening...")
        audio = r.listen(source)
    if audio != None:
        print("Speech recognition in progress...")
        try:
            # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
            text = r.recognize_google(audio)
            print(": "+text)
        except LookupError:
            print("Google didn't understand that")
        except sr.UnknownValueError:
            print("Just being quiet?")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
    return text


def speak(text):
    tts.say(text)
    tts.runAndWait()
    # speech = gTTS(text=text, lang=lang, slow=False, tld="com.au")
    # speech.save("welcome1.mp3")
    # playsound.playsound("welcome1.mp3")


def openai(text):
    ai_text = ""
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": text}
            ])
        ai_text = completion.choices[0].message.content
    except openai.error.RateLimitError:
        print("Damn it, rate limitation error again!")
    return ai_text


def ai():
    ai_text = ""
    try:
        pass
    except:
        pass
    return ai_text


while True:

    text = listen(mic)

    if text != "":
        print(text)
        speak(text)

    if ai_name in text:
        words = text.split()
        print(words)
        new_string = ' '.join(words[1:])
        print(new_string)
        ai_text = ""

        ai_text = openai(text)
        # ai_text = ai(text)

        speak(ai_text)

    if "stop" in text:
        print("Stopping!")
        speak("Stopping!")
        break
