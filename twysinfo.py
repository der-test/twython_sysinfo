#!/usr/bin/env python
# coding: utf-8
import sys
# os for cmd
import os
# Twython
from twython import Twython
# config
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

# api call
api = Twython(parser.get('config', 'apiKey'),parser.get('config', 'apiSecret'),parser.get('config', 'accessToken'),parser.get('config', 'accessTokenSecret'))

# Console output for debug
print "Gathering sysinfo..."

# Get date ,format: DD.MM.YY HH:MM
cmd = 'date +"%d.%m.%y %H:%M"'
time = os.popen(cmd).readline().strip()

# Get CPU temperature and set variable
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

# IP, change Adresse to the output of ifconfig if other than de or en
#en
#cmd = '/sbin/ifconfig wlan0 | grep -Po \'t addr:\K[\d.]+\''
#de
cmd = '/sbin/ifconfig wlan0 | grep -Po \'t Adresse:\K[\d.]+\''
ip  = os.popen(cmd).readline().strip()

# External IP
# install dnsutils to use dig
cmd = 'dig +short myip.opendns.com @resolver1.opendns.com'
extip  = os.popen(cmd).readline().strip()

# Console output for debug
print "Finished gathering sysinfo!"
print "Tweeting..."

# tweet v1
# tweet = 'CPU temperature: '+temp+' C. ' 'The date and time is: '+time+'. ' 'Memory usage: ' + str(usedmb) + 'M of ' + str(totalmb) + 'M or ' + str(percent) + '%. IP: '+extip
# tweet v2
tweet = time+' Uhr\nCPU: '+temp+' C˚\nRAM: ' + str(usedmb) + '/' + str(totalmb) + 'M or ' + str(percent) + '%\nIP: '+extip
api.update_status(status = tweet)

#Console output for debug
print "Finished tweeting! Submitted tweet:"
print tweet
