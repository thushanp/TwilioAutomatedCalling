# Download the library from twilio.com/docs/libraries
from twilio.rest import Client

# Get these credentials from http://twilio.com/user/account
account_sid = "ACf0bef51e5a407e3ace365f87a23ccb46"
auth_token = "5e7b2c6563764d0d62dc00e18e1b5853"
client = Client(account_sid, auth_token)

# Make the call
call = client.api.account.calls\
      .create(to="+16175159619",  # Any phone number
              from_="+14054001401", # Must be a valid Twilio number
              url="https://www.dl.dropboxusercontent.com/s/8twqvptu71pq8rd/01%20Frank%20Ocean%20-%20Lost_1.mp3?dl=0")

print(call.sid)