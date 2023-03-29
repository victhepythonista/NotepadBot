import os
import sys
import shutil
import win32gui
import pyautogui
import win32com.client
import re


def ScanWindowName(pattern, window_name):
	# check if the patter appears
	# in the screens name
	pattern = pattern.lower()
	window_name = window_name.lower()
	if re.search(pattern, window_name ):
		return True
	return False

def GetAllWindows():
    # get all opened, active. even minimized
    # window
    '''
    return type : list
    '''
    windows_list = []
    def EnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            # BUG ... dont delete the if..DONT !!
            window_details = hwnd, win32gui.GetWindowText(hwnd)
            windows_list.append(window_details)

    win32gui.EnumWindows(EnumHandler, None)
    return windows_list

def  SearchForWindowWithName(name , action =None):
    windows_list = GetAllWindows()
    matches = []
    for hwnd,window_text  in windows_list:
        if ScanWindowName(name, window_text):
                matches.append((hwnd,window_text))
                print("Match found  :",window_text)
                #    we perform an aaction to the window
                if action is not None:
                    action(hwnd, window_text)
    return matches

def SendAltKey():
    # this prevents the BUG in pywin32 of
    # swin32.SetupForegroundWindow
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys('%')


def GetWindowCenter(hwnd):
    # useful for apps like Text Editors ..I get me....you dont :
    x,y,w,h = win32gui.GetWindowRect(hwnd)
    c_x,c_y = x + w/2 , y + h/2
    return c_x,c_y

def ClickOnScreen(hwnd):
    # click on a point i on the screen
    rect = win32gui.GetWindowRect(hwnd)
    pyautogui.click(GetWindowCenter(hwnd))

def GetRandomWindow():
	# return the handle of a random window
	pass


if __name__ == '__main__':
    all_w = SearchForWindowWithName("Untitled - Notepad")

    print(all_w)