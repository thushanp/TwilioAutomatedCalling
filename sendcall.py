from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf0bef51e5a407e3ace365f87a23ccb46"
# Your Auth Token from twilio.com/console
auth_token  = "5e7b2c6563764d0d62dc00e18e1b5853"

client = Client(account_sid, auth_token)

call = client.calls.create(to="+16175159619", 
    					   from_="+14054001401",
    					   url="http://thushanp.github.io/parth")

print(call.sid)