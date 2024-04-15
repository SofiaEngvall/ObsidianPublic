import ctypes
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import time
import webbrowser

# get handles to audio devices
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# open Web browser, unmute, and set volume to 100%
x = 0
while (x == 0):

    # open web browser
    webbrowser.open_new(
        "https://www.youtube.com/watch?v=dQw4w9WgXcQ&autoplay=1")

    # unmute the volume no matter what
    volume.SetMute(False, None)

    # set volume 100%
    volume.SetMasterVolumeLevel(-0.0, None)

    time.sleep(20)
