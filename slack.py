#!/usr/bin/python

#   Created by Wesley Archer at Raspberry Coulis                                                    #
#   Website: https://www.raspberrycoulis.co.uk | Twitter: @raspberrycoulis                          #
#                                                                                                   #
#   1. Intro:                                                                                       #
#                                                                                                   #
#   This Python script sends notifications to a dedicated Slack channel whenever movement is        #
#   detected in MotionEye OS.                                                                       #
#                                                                                                   #
#   You will need to create a free Slack account over at https://slack.com/ and create an incoming  #
#   webhook by visiting https://my.slack.com/services/new/incoming-webhook/. I recommend creating   #
#   a dedicated Slack channel (i.e. #motioneyeos), but you can also add a custom icon and name      #
#   to make it look the part too!                                                                   #
#                                                                                                   #
#   2. Customising your Slack notification:                                                         #
#                                                                                                   #
#   You can customise the message sent to Slack by editing the data string below.                   #
#                                                                                                   #
#   The string must be within curly brackets and start with {"text": }. Links can be included       #
#   between <> - i.e. <https://www.raspberrycoulis.co.uk> and text can be displayed using | so this #
#   <https://www.raspberrycoulis.co.uk|Raspberry Coulis> would be a link to Raspberry Coulis!       #
#                                                                                                   #
#   To emphasise text, place words you want in bold between two asterix - i.e. *this is bold!*      #
#                                                                                                   #
#   Split text onto a new line with "\n" (without the quotation marks) so "Hello\nWorld!" becomes   #
#                                                                                                   #
#   Hello                                                                                           #
#   World!                                                                                          #
#                                                                                                   #
#   Remember to enclose your custom text message within quotation marks though!                     #
#                                                                                                   #
#   3. This is my example:                                                                          #
#                                                                                                   #
#   '{"text": "Motion Detected!\nView the *<http://IP.ADD.RE.SS|live stream>* now!"}'               #

import urllib, urllib2

url = 'INSERT-SLACK-INCOMING-WEBHOOK-URL-HERE'          # Add your Slack incoming Webhook URL here (starts https://hooks.slack.com)
data = '{"text": "Motion Detected!\nView the *<http://IP.ADD.RE.SS|live stream>* now!"}'            # See above to customise message.

req = urllib2.Request(url, data, {'Content-Type': 'application/json'})
f = urllib2.urlopen(req)
f.close()
