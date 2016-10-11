# Slack Notifications in MotionEye OS

### Intro
This Python script sends notifications to a dedicated [Slack](https://slack.com "Slack: Be less busy") channel whenever movement is detected in [MotionEye OS](https://github.com/ccrisan/motioneyeos/releases).

You will need to create a free Slack account over at https://slack.com/ and create an incoming webhook by visiting https://my.slack.com/services/new/incoming-webhook/. I recommend creating a dedicated Slack channel (i.e. #motioneyeos), but you can also add a custom icon and name to make it look the part too! There is also a Slack app (iOS and Android), so installing this will also give you notifications when you are out and about.

### Customising your Slack notification:                                                         

You can customise the message sent to Slack by editing the data string below. The string must be within curly brackets and start with ```{"text": }```. Links can be included between ```<>``` - i.e. ```<https://www.raspberrycoulis.co.uk>``` and text can be displayed using ```|``` so this ```<https://www.raspberrycoulis.co.uk|Raspberry Coulis>``` would be a link to [Raspberry Coulis](https://www.raspberrycoulis.co.uk "Raspberry Coulis: Raspberry Pi Projects, Tutorials & Reviews")!

To emphasise text, place words you want in bold between two asterix - i.e. ```*this is bold!*``` becomes **```this is bold!```**

Split text onto a new line with ```\n``` (without the quotation marks) so ```Hello\nWorld!``` becomes:

```
Hello                                                                                           
World!
```

Remember to enclose your custom text message within quotation marks though!

### This is my example:

```'{"text": "Motion Detected!\nView the *<http://IP.ADD.RE.SS|live stream>* now!"}'```

# Installation
MotionEye OS is not like Raspbian. You cannot use certain commands as you would normally (such as git clone), so we’ll have to create our Python script manually. We also do not need to use sudo as we’re already logged in as root by default. Our script needs to live in the data folder, so let’s go there and create slack.py using Nano:

```
cd /data
nano slack.py
```

Copy and paste the contents of slack.py into this new file, making sure you add your Webhook URL into the relevant place. Press Ctrl + X to exit, pressing Y to save. You will need to make your script executable, and this can be done from the terminal by running:

```
chmod +x slack.py
```

You can quickly test this script out from the terminal by running (assuming you are still in the data folder):

```
python slack.py
```

## Setting up MotionEye OS

Now that we have our script, we need to tell MotionEye OS to use it when it detects motion. To do this, log in and then go to the **Motion Notifications** menu and then turn on **Run A Command**. You then need to specify which command to run, which will be the Python script you just created. This will be **/data/slack.py**. Click **Apply** once done to confirm the changes.

## Test it out!

Double check that everything works by waving your hand in front of your MotionEye OS camera. All being well, you should receive a Slack notification alerting you.
