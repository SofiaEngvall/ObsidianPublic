import ctypes
import random
import time

x = 0
while(x==0):
    mouse_x = random.randint(10, 1800)
    mouse_y = random.randint(10, 1800)
    
    #API documentation https://learn.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-setcursorpos
    user_handle = ctypes.WinDLL("User32.dll")
    user_handle.SetCursorPos(mouse_x, mouse_y)
    #user_handle = ctypes.windll.user32.SetCursorPos(mouse_x,mouse_y)
    time.sleep(1)

