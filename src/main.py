# A simple project that changes the mac address of your computer
# Created by Donal Moloney on January 7 2019

#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i", "--interface",dest="interface", help="Interface to change its MAC address")
parser.add_option("-m", "--mac",dest="new_mac", help="New mac address")

(options, arguments) = parser.parse_args() # can access value for interface or new_mac by doing options.new_mac or options.interface to get values out

interface = options.interface
new_mac = options.new_mac

print("[+] Changing MAC address for " + interface + " to " + new_mac)

subprocess.call(["ifconfig",interface,"down"], shell = True) #disabling wlan0
subprocess.call(["ifconfig",interface,"hw","ether",new_mac], shell = True) #changing mac address of wlan
subprocess.call(["ifconfig",interface,"up"], shell = True) #enabeling wlan0
