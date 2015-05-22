from flask import Flask, request, redirect, Response
from twilio.rest import TwilioRestClient
import twilio.twiml
import requests
import json
 
app = Flask(__name__)



account_sid = "we3143ew"
auth_token = "we21234asdasd"
client = TwilioRestClient(account_sid, auth_token)

@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond to incoming text message."""
    resp = twilio.twiml.Response()
    msgBody = request.values.get('Body')
    print "msgBody", msgBody

    return str(resp)
 
@app.route("/callout", methods=['POST'])
def callOut():
    number = json.loads(request.data)['number']
    # Make the call
    call = client.calls.create(
        to=number, # Any phone number
        from_="+12694643250",
        #url="http://www.ispeech.org/p/generic/getaudio?text=Hi%20from%20call%20hub%2C&voice=usenglishfemale&speed=0&action=convert"
	url="http://www.ispeech.org/p/generic/getaudio?text=BlueJeans%20offers%20premium%20facilities%20like%20recording.%20Give%20it%20a%20try%3F%2C&voice=usenglishfemale&speed=0&action=convert"
    )
    return str("Success")

@app.route("/sms", methods=['POST'])
def Sms():
    number = json.loads(request.data)['number']
    # Send a SMS
    call = client.messages.create(
        to=number, # Any phone number
        from_="+12694643250",
        body="Hello from CallHub"
    )
    return str("Success")

@app.route("/twiml.xml", methods=["GET"])
def twiml():
    return Response("<Response><Say>You are now entering the conference line.</Say><Dial><Conference>foo</Conference></Dial></Response>", mimetype='text/xml')

if __name__ == "__main__":
    app.run(debug=True)
