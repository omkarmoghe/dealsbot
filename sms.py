from twilio.rest import TwilioRestClient
import globals

def send_SMS (message):
    # import auth codes for Twilio
    account_sid = globals.ACCOUNT_SID
    auth_token = globals.AUTH_TOKEN
    to_phone = globals.TO_PHONE
    from_phone = globals.TWILIO_PHONE

    client = TwilioRestClient(account_sid, auth_token)
     
    message = client.messages.create(to=to_phone, from_=from_phone, body=str(message))
