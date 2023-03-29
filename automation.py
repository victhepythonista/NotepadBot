import pyautogui
import os
import win32gui
import platform
import subprocess




def OpenNotePad():
    assert platform.system() == 'Windows', "THIS CODE WAS DESIGNED TO RUN ON WINDOWS.....!"
    print("opening notepad")
    subprocess.Popen(["notepad", ])
    print("Notepad opened ")


def TypeKey(key):
    pyautogui.keyDown(key)


def GetAllWindows():
    WINDOWS = []

    def EnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            # BUG ... dont delete the if..DONT !!
            window_details = hwnd, win32gui.GetWindowText(hwnd)
            WINDOWS.append(window_details)

    win32gui.EnumWindows(EnumHandler, None)
    return WINDOWS


if __name__ == '__main__':
    OpenNotePad()