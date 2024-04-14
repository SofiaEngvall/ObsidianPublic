import ctypes

# reference:
# MessageBoxW: https://docs.microsoft.com/en-us/windows/win32/api/winuser/nf-winuser-messageboxw

# inputs:
#  int MessageBoxW(
# [in, optional] HWND    hWnd,
# [in, optional] LPCWSTR lpText,
# [in, optional] LPCWSTR lpCaption,
# [in]           UINT    uType
# );

user_handle = ctypes.WinDLL("User32.dll")
k_handle = ctypes.WinDLL("Kernel32.dll")

hWnd = None
lpText = "Hello World!"
lpCaption = "Hello Students!"
uType = 0x00000001

response = user_handle.MessageBoxW(hWnd, lpText, lpCaption, uType)

# LCTF{hello_w0rld}
err = k_handle.GetLastError()
if err != 0:
    print("Error code is: " + err)
    exit(1)

if response == 1:
    print("User clicked OK!")
else:
    print("User clicked cancel")
