#!/usr/bin/env python3

#has to be run with sudo

import keyboard
keys = keyboard.record(until ='ENTER')
keyboard.play(keys)
