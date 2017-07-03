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
    r.gather(timeout="10", 
             action="http://twimlbin.com/external/0d2c3c0909a0e23e")
 
    return str(r)
 
call = client.calls.create(to="+16175159619", from_="+14054001401",
                           url="https://www.dl.dropboxusercontent.com/s/8twqvptu71pq8rd/01%20Frank%20Ocean%20-%20Lost_1.mp3?dl=0")
 
if __name__ == "__main__":
    app.run()