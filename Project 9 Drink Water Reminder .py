# RULES:- 
# Exercise 11 - Drink Water Reminder
# Write a python program which reminds you of drinking water every hour or two. Your program can either beep or send desktop notifications for a specific operating system



# coding ---------------------------------------

import os
import time 

REPEAT_INTERVAL = 3600 # Repeat frequency in seconds


# NOTE: this oascript and all are only available for mac. for windows we can get it just by googling "windows display notification"
while True:
    command = "osascript -e \'say \"Hey Harry drink water\"\'; osascript -e \'display alert \"Hey Harry, Drink water\"\'"
    os.system(command)
    time.sleep(REPEAT_INTERVAL)