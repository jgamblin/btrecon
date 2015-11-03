
#!/usr/bin/env python
# Name:     btrecon.py
# Purpose:  Bluetooth Scanner 
# By:       Jerry Gamblin
# Date:     02.11.15
# Modified  02.11.15
# Rev Level 0.5
# -----------------------------------------------

import os
import re
import time
import sys
import subprocess
import readline

def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)

def red(text):
    return color(text, 31)


def blink(text):
    return color(text, 5)


def green(text):
    return color(text, 32)


def blue(text):
    return color(text, 34)


#clean up old files
os.system("rm -rf devices.txt")
os.system("rm -rf btaddresses.txt")

print "\n"
print "Finding Bluetooth Devices..."
os.system("hcitool -i hci0 scan > devices.txt")
print "Found The Following Devices:"
os.system("cat devices.txt | grep -i '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}'")
os.system("cat devices.txt | grep -o '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}' > btaddresses.txt")
b = open('btaddresses.txt')
macs = b.readlines()
b.close()
print "\n"
print "Starting Information Gathering"
print "\n"
for mac in macs:
	print (green("Information about %s" % mac))
	subprocess.call("hcitool name %s" % mac, shell=True)
	print "\n"
	subprocess.call("hcitool info %s" % mac, shell=True)
	print "\n"	
	subprocess.call("sdptool records %s" % mac, shell=True)
	print "\n"
	subprocess.call("sdptool browse %s" % mac, shell=True)	
	print "\n"
print "\n"



