from flask import Flask

from twilio import twiml
from twilio.rest import TwilioRestClient


account_sid = "ACf0bef51e5a407e3ace365f87a23ccb46"
auth_token = "5e7b2c6563764d0d62dc00e18e1b5853"
client = TwilioRestClient(account_sid, auth_token)

app = Flask(__name__)
 
 
@app.route('/voice', methods=['POST'])
def detect_humans():
    r = twiml.Response()
    r.say("Machines don't press keys, but humans do. Press a key now.")
    r.gather(timeout="10", 
             action="http://twimlbin.com/external/0d2c3c0909a0e23e")
    r.say("Too bad, you did not press a key. Goodbye!")
 
    return str(r)
 
call = client.calls.create(to="YOUR_NUMBER", from_="YOUR_TWILIO_NUMBER",
                           url="YOUR_VOICE_URL")
 
if __name__ == "__main__":
    app.run()