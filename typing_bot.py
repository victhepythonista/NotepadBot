__author__ = "Victor Kipkemboi"
__copyright__ = "Copyright (C) 2023"
__license__ = "Public Domain"
__version__ = "1.0"

# ENJOY :)

import pyautogui
import os
import win32gui
import sys
import time



 
from automation import OpenNotePad, TypeKey
from backend import SearchForWindowWithName , SendAltKey


class TypingBot:
	def __init__(self, app_loading_time = 3, mid_key_time = 0.5, time_before_typing = 2):
		self.app_loading_time = app_loading_time
		self.mid_key_time = mid_key_time
		self.time_before_typing = time_before_typing
		self.notepad_hwnd = 0

	def Type(self, text):
		assert type(text) == str, f'Invalid data required text but got {type(text)}'
		print(f'Please wait  {self.app_loading_time} seconds please ....')
		time.sleep(self.time_before_typing)
		for ch in text:
			time.sleep(self.mid_key_time)

			if win32gui.GetForegroundWindow() != self.notepad_hwnd:
				SendAltKey()

				try:
					win32gui.SetForegroundWindow(self.notepad_hwnd)
				except:
					print("You may have closed notepad ..Terminating")
					return
			TypeKey(ch)


	def GetFreshNotepad(self):
		# get the hwnd for the newly opened notepad
		notepads = SearchForWindowWithName("Untitled - Notepad")
		print("Notepads found  " , notepads)
		notepad_hwnd = notepads[0][0]
		print("HWND  found -->" , notepad_hwnd)
		self.notepad_hwnd = notepad_hwnd


	def TypeOnNotepad(self,text  ):
		OpenNotePad()
		time.sleep(2)# allow time for notepad to open
		
		self.GetFreshNotepad()

	 
		time.sleep(self.app_loading_time)
		self.Type(text)



	def TypeFileOnNotepad(self,  file_path):
		# open a file and write its contents on notepad 
		if not os.path.isfile(file_path):
			# no such file 
			print("error locating file  " , file_path)
			return
		OpenNotePad()
		self.GetFreshNotepad()
		text = ""
		with open( file_path , "r") as f:
			text = f.read() 
		self.Type(text)

		
if __name__ == '__main__':
	# TypingBot().TypeOnNotepad('Typing this data on notepad')
	TypingBot().TypeFileOnNotepad("zen_of_python.txt")