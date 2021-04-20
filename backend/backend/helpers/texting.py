from decouple import config
from twilio.rest import Client 

def sendTextMessage(to, message):
    client = Client(config('TWILIO_SID'), config('TWILIO_SECRET')) 
    
    message = client.messages.create(
                                from_='+15005550006',  
                                to=config('TWILIO_TEST_NUMBER'),
                                body=message
                            )
    
    return message