# A simple project that changes the mac address of your computer
# Created by Donal Moloney on January 7 2019
#!/usr/bin/env python

import subprocess

interface = input("Enter an interface to change for example: wlan0\n")
new_mac = input("Enter a new MAC address example: 00:11:22:33:44:77\n")

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call("ifconfig "+interface+" down", shell = True) #disabling wlan0
subprocess.call("ifconfig "+interface+" hw ether "+ new_mac, shell = True) #changing mac address of wlan
subprocess.call("ifconfig "+interface+" up", shell = True) #enabeling wlan0
