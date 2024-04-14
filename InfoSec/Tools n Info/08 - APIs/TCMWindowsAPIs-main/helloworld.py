import ctypes

user_handle = ctypes.WinDLL("User32.dll")
# ctypes.Windll.user32.MessageBox
# our API
'''
int MessageBoxW(
  [in, optional] HWND    hWnd,
  [in, optional] LPCWSTR lpText,
  [in, optional] LPCWSTR lpCaption,
  [in]           UINT    uType
);
'''

hWnd = None
lpText = "Hello World!"
lpCaption = "Hello Students"
uType = 0x000000001
# uType = 0x000000001

x = 0
while (x == 0):
    response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

    if response == 1:
        print("User clicked ok!")
        x = 1
    else:
        print("User clicked cancel")
        x = 0
