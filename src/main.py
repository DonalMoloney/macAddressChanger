# A simple project that changes the mac address of your computer
#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell = True) #disabling wlan0
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell = True) #changing mac address of wlan
subprocess.call("ifconfig wlan0 up", shell = True) #enabeling wlan0
