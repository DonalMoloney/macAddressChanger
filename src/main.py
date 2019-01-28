# A simple project that changes the mac address of your computer
#!/usr/bin/env python

import subprocess

interface = "wlan0"
new_mac = "00:11:22:33:44:77"

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig "+interface+" down", shell = True) #disabling wlan0
subprocess.call("ifconfig "+interface+" hw ether "+ new_mac, shell = True) #changing mac address of wlan
subprocess.call("ifconfig "+interface+" up", shell = True) #enabeling wlan0
