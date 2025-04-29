#!/usr/local/bin/python

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import json
import binascii
from secrets import FLAG
import random

class SeerOracle:
    def __init__(self, key):
        self.key = key

    def generate_token(self):
        fortunes = [
            "The stars align in your favor.",
            "A journey of the heart awaits.",
            "Secrets will be revealed in due time.",
            "The winds of change are blowing.",
            "A shadow from the past will reappear.",
            "Trust the whispers of the night.",
            "A new dawn brings unexpected gifts.",
            "The universe is conspiring for you.",
            "A hidden path will soon be illuminated.",
            "The answer lies within.",
            "A mysterious encounter will change your course.",
            "The tides of fate are turning.",
            "A forgotten dream will resurface.",
            "The key to your future is in your hands.",
            "A voice from the past will guide you.",
            "The moon holds secrets for you.",
            "A new chapter begins with a single step.",
            "The stars have a message for you.",
            "A veil will be lifted from your eyes.",
            "The winds carry whispers of destiny.",
            "A chance meeting will alter your path.",
            "The sands of time are shifting.",
            "A hidden truth will come to light.",
            "The universe is listening to your desires.",
            "A forgotten memory will bring clarity.",
            "The stars are watching over you.",
            "A new opportunity is on the horizon.",
            "The past and future will collide.",
            "A gentle breeze brings new beginnings.",
            "The night sky holds your answers.",
            "A secret will be unveiled.",
            "The path ahead is shrouded in mystery.",
            "A new ally will appear in your life.",
            "The stars are aligning for a new journey.",
            "A whisper of the past will guide you.",
            "The universe is weaving your destiny.",
            "A hidden door will open for you.",
            "The winds of fortune are in your favor.",
            "A forgotten wish will be granted.",
            "The stars have a plan for you.",
            "A new light will shine on your path.",
            "The universe is unfolding as it should.",
            "A shadow will reveal its true form.",
            "The night holds a secret for you.",
            "A new beginning is just around the corner.",
            "The stars are guiding your steps.",
            "A hidden treasure will be uncovered.",
            "The universe is whispering your name.",
            "A forgotten promise will be fulfilled.",
            "The winds of change are at your back.",
            "A new perspective will bring clarity.",
            "The stars are aligning for your success.",
            "A hidden talent will be discovered.",
            "The universe is opening doors for you.",
            "A forgotten path will be rediscovered.",
            "The night sky is full of possibilities.",
            "A new friend will bring joy.",
            "The stars are shining on your dreams.",
            "A hidden strength will be revealed.",
            "The universe is guiding your journey.",
            "A forgotten love will be rekindled.",
            "The winds of destiny are blowing.",
            "A new adventure awaits.",
            "The stars are aligning for a new beginning.",
            "A hidden message will be uncovered.",
            "The universe is working in your favor.",
            "A forgotten truth will be revealed.",
            "The night holds a promise for you.",
            "A new path will be illuminated.",
            "The stars are watching over your journey.",
            "A hidden blessing will be discovered.",
            "The universe is aligning for your success.",
            "A forgotten dream will come true.",
            "The winds of fortune are at your side.",
            "A new ally will join your quest.",
            "The stars are guiding your destiny.",
            "A hidden opportunity will arise.",
            "The universe is conspiring for your happiness.",
            "A forgotten memory will bring joy.",
            "The night sky is full of wonder.",
            "A new beginning is on the horizon.",
            "The stars are aligning for your future.",
            "A hidden truth will bring peace.",
            "The universe is unfolding in your favor.",
            "A forgotten wish will be remembered.",
            "The winds of change are in your sails.",
            "A new perspective will bring insight.",
            "The stars are shining on your path.",
            "A hidden strength will be your guide.",
            "The universe is opening new doors.",
            "A forgotten love will find its way back.",
            "The night holds a mystery for you.",
            "A new adventure is calling.",
            "The stars are aligning for your journey.",
            "A hidden talent will shine.",
            "The universe is weaving your dreams.",
            "A forgotten promise will be kept.",
            "The winds of destiny are at your back.",
            "A new light will guide your way.",
            "The stars are watching over your dreams."
        ]
        iv = os.urandom(16)  # Random IV for each encryption
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = json.dumps({"flag": FLAG, "fort": random.choice(fortunes)}).encode()
        return iv + cipher.encrypt(pad(plaintext, AES.block_size))
    
    def fortune_from_token(self, message):
        try:
            iv = message[:16]
            enc = message[16:]
            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(enc), 16).decode()
        except:
            return(False, "Your token is not from me, come back with a real token and I can read your fortune")
        try:
            d = json.loads(pt)
            fortune = d['fort']
            assert d['flag'] == FLAG
            return(True, fortune)
        except:
            return(False, "The mystics are unhappy, your fortune seems corrupted.")


def print_menu(banner=False):
    if(banner) :
        print("""
.-.   .-.  .--.   .---. .-. .---.   .--.  .-.       .----..----..----..----. 
|  `.'  | / {} \\ /   __}| |/  ___} / {} \\ | |      { {__  | {_  | {_  | {}  }
| |\\ /| |/  /\\  \\\\  {_ }| |\\     }/  /\\  \\| `--.   .-._} }| {__ | {__ | .-. \\
`-' ` `-'`-'  `-' `---' `-' `---' `-'  `-'`----'   `----' `----'`----'`-' `-'
""")
    print("""
1. Ask the magical seer for a fortune token
2. Ask the magical seer to read a fortune token""")

def main():
    tokens_generated = 0
    key = os.urandom(16)  # Random key for AES
    seer = SeerOracle(key)
    display_banner = True
    while True:
        print_menu(display_banner)
        display_banner=False
        try:
            choice = int(input("> "))
            if choice == 1:
                if tokens_generated < 1:
                    print(f"The mystics have spoken to me. They have given you the magical token {seer.generate_token().hex()}, keep it safe.")
                    tokens_generated += 1
                else:
                    print("You have already been blessed with a magical token! Have you not safeguarded it? I shall give you no others.")
            elif choice == 2:
                token = input("Very well, give me the token to read: ")
                try:
                    token_bytes = binascii.unhexlify(token)
                    valid, fortune = seer.fortune_from_token(token_bytes)
                    if valid:
                        print(f"Ahem, your fortune is as follows: \"{fortune}\"")
                    else:
                        print(fortune)
                except binascii.Error:
                    print("The token you provided is not valid. Please provide a valid token.")
            else:
                print("I do not understand your request. Please choose a valid option.")
                display_banner=True
        except ValueError:
            print("I do not understand your request. Please choose a valid option.")
            display_banner=True

if __name__ == "__main__":
    main()
