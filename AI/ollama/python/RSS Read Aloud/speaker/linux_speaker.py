# linux_speaker.py - Class to simplify the use of espeak-ng
# version 1.0
# by Sofia Engvall - FixIt42, 2025-05-04

# espeak-ng installation:
# sudo apt install espeak
# pip install espeakng


from espeakng import ESpeakNG

VOICE = "en-us+m3"  # Example: male voice 3, you can list more via espeak
SPEED = 150  # Words per minute

class Speaker:
    def __init__(self, also_print=False, speed=SPEED):
        self.esng = ESpeakNG()
        self.esng.speed = speed
        self.also_print = also_print
        self.set_voice(VOICE)

    def set_voice(self, voice_name):
        self.esng.voice = voice_name

    def print_voices(self):
        # Just a few examples; for full list, run: `espeak-ng --voices`
        voices = ["en", "en-us", "en+f2", "en+m1", "en+m3", "en+croak"]
        for v in voices:
            print(v)
        print(f"Current voice: {self.esng.voice}")

    def set_speed(self, speed):
        self.esng.speed = speed

    def tell_speed(self):
        self.speak(f"My speaking rate is set to {self.esng.speed} words per minute.")

    def speak(self, text):
        if self.also_print:
            print(text)
        try:
            self.esng.say(text)
        except Exception as e:
            print(f"Error in TTS: {e}")

if __name__ == "__main__":
    s = Speaker()
    s.print_voices()
