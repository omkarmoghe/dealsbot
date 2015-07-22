# dealsbot

A bot that searches /r/buildapcsales for desired components within the specified price, etc. and sends you an SMS when it finds a deal.

Originally designed to be run on my Raspberry Pi.

-----

# Building
In order to run the bot you will need a Twilio account with an activated and registered Twilio number and working phone number with SMS enabled.

Create a file in the directory named `globals.py`

Add the following code to the `globals.py` file, replacing the fields with your Twilio and phone info.

```python
# your Twilio account sid
ACCOUNT_SID = "TWILIO ACCOUNT SID"

# your Twilio auth token
AUTH_TOKEN = "TWILIO AUTHENTICATION TOKEN"

# the phone number you want to send the SMS to.
# NOTE: this number must me verified on Twilio if you 
#       are using a trial account.
#       FORMAT: "+1234567890"
TO_PHONE = "YOUR PHONE"

# your Twilio phone number
# FORMAT: "+1234567890"
TWILIO_PHONE = "YOUR TWILIO PHONE"
```
