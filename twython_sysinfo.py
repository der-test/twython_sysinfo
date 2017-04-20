#!/usr/bin/env python
# coding: utf-8

import sys
# os for cmd
import os
from twython import Twython

# Change your_data to the strings from you own twitter app
apiKey = 'your_data'
apiSecret = 'your_data'
accessToken = 'your_data'
accessTokenSecret = 'your_data'
api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)

# Console output for debug
print "Gathering sysinfo..."

# Get date
cmd = 'date'
time = os.popen(cmd).readline().strip()

# Get CPU temperature and set temp
cmd = '/opt/vc/bin/vcgencmd measure_temp'
line = os.popen(cmd).readline().strip()
temp = line.split('=')[1].split("'")[0]

# Get memory usage and calculate percentage
cmd = 'awk \'/MemTotal/ { print $2 }\' /proc/meminfo'
total = int(os.popen(cmd).readline().strip())
cmd = 'awk \'/MemFree/ { print $2 }\' /proc/meminfo'
free = int(os.popen(cmd).readline().strip())
used = total - free
percent = (used * 100) / total
usedmb = used / 1024
totalmb = total / 1024

# IP, change Adresse to the output of ifconfig
#en
#cmd = '/sbin/ifconfig wlan0 | grep -Po \'t addr:\K[\d.]+\''
#de
cmd = '/sbin/ifconfig wlan0 | grep -Po \'t Adresse:\K[\d.]+\''
ip  = os.popen(cmd).readline().strip()

# Console output for debug
print "Finished gathering sysinfo!"
print "Tweeting..."

# Load last snpshot the from motion standard image folder
# motion config snapshot_interval must be larger than 0
photo = open('/var/lib/motion/lastsnap.jpg', 'rb')
tweet = 'CPU temperature: '+temp+' C. ' 'The date and time is: '+time+'. ' 'Memory usage: ' + str(usedmb) + 'M of ' + str(totalmb) + 'M or ' + str(percent) + '%. IP: '+ip
api.update_status_with_media(status=tweet, media=photo)

# Uncomment the following line to send a tweet without an attached image
# and add a comment to the previous line instead

api.update_status(status = tweet)

#Console output for debug
print "Finished tweeting!"
