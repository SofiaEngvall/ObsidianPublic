import win32com.client

SPEAKING_SPEED = 4  # -10 to 10

class Speaker():
    def __init__(self):
        self.tts = win32com.client.Dispatch('SAPI.Spvoice')

        # self.print_voices()
        self.set_voice(2)
        self.set_speed(SPEAKING_SPEED)
        # self.tell_speed()

    def set_voice(self, voice_number):
        voices = self.tts.GetVoices()
        self.tts.Voice = voices.Item(voice_number)

    def print_voices(self):
        voices = self.tts.GetVoices()
        for voice in voices:
            print(voice.GetDescription())
        print(f"Current voice: {self.tts.Voice.GetDescription()}")

    def set_speed(self, speed):
        self.tts.Rate = speed

    def tell_speed(self):
        self.speak(f"My speaking rate is set to {self.tts.Rate}.")

    def speak(self, text):
        #print(text)
        self.tts.Speak(text)
