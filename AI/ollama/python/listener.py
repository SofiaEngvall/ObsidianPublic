import speech_recognition as sr
import speaker

class Listener():
    def __init__(self):
        self.sr = sr.Recognizer()
        self.mic = sr.Microphone()
        print("Getting background noice level")
        with self.mic as source:
            self.sr.adjust_for_ambient_noise(source, 2)
        self.s = speaker.Speaker()

    def listen(self):
        text = ""
        with self.mic as source:
            source.pause_threshold = 15
            source.non_speaking_duration = 2 #0.5
            source.energy_threshold = 40  # 300?
            source.dynamic_energy_threshold = False

            print("Listening...")
            audio = self.sr.listen(source)

        if audio != None:
            print("Speech recognition in progress...")
            try:
                # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                text = self.sr.recognize_google(audio)
            except LookupError:
                self.s.speak("Could you repeat that please.")
            except sr.UnknownValueError:
                self.s.speak("hmm...")
            except sr.RequestError as error:
                self.s.speak(
                    f"I couldn't reach google (error {error}).")
        return text

    def record(self):
        with self.mic as source:
            source.pause_threshold = 1
            return self.sr.listen(source, phrase_time_limit=None, timeout=None)

    def get_name(self):
        name = ""
        while name == "":
            name = self.listener.listen()
            if name == "":
                self.s.speak(
                    "Could you repeat that, please?")
        return name
    