from flask import Flask, request, redirect, Response
from twilio.rest import TwilioRestClient
import twilio.twiml
import requests
import json
 
app = Flask(__name__)


#account_sid = "AC9deb9d2bab249c5889e468dba126b9dd"
#auth_token = "810f5eb6e8b219e96c80bc6d0c94dc44"
#from_="+14434062749", # Must be a valid Twilio number

account_sid = "AC0e6675808b1d2aefc45b0b4d1df066c8"
auth_token = "2d84d7b7d22ff9d91779901dbadda7ad"
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
