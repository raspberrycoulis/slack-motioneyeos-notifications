# Slack Notifications in MotionEye OS

### Intro
This Python script sends notifications to a dedicated [Slack](https://slack.com "Slack: Be less busy") channel whenever movement is detected in [MotionEye OS](https://github.com/ccrisan/motioneyeos/releases).

You will need to create a free Slack account over at https://slack.com/ and create an incoming webhook by visiting https://my.slack.com/services/new/incoming-webhook/. I recommend creating a dedicated Slack channel (i.e. #motioneyeos), but you can also add a custom icon and name to make it look the part too!                                                    

### Customising your Slack notification:                                                         
                                                                                                   
You can customise the message sent to Slack by editing the data string below. The string must be within curly brackets and start with ```{"text": }```. Links can be included between ```<>``` - i.e. ```<https://www.raspberrycoulis.co.uk>``` and text can be displayed using | so this ```<https://www.raspberrycoulis.co.uk|Raspberry Coulis>``` would be a link to [Raspberry Coulis](https://www.raspberrycoulis.co.uk "Raspberry Coulis: Raspberry Pi Projects, Tutorials & Reviews")!     

To emphasise text, place words you want in bold between two asterix - i.e. ```*this is bold!*```

Split text onto a new line with ```\n``` (without the quotation marks) so ```Hello\nWorld!``` becomes   

```
Hello                                                                                           
World!
```

Remember to enclose your custom text message within quotation marks though!

### This is my example:                                                                          

```'{"text": "Motion Detected!\nView the *<http://IP.ADD.RE.SS|live stream>* now!"}'```
