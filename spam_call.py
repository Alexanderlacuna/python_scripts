from twilio.rest import Client
TWILIO_PHONE_NUMBER = "+13605854882"

DIAL_NUMBER = ["+254791872846",]

TWIML_INSTRUCTIONS_URL = "http://static.fullstackpython.com/phone-calls-python.xml"



client = Client("AC5e7934b46fb7fc500b975f818c9d33f5","bda777207e511dff0c023d9975157275")

import time 

def dial_numbers(numbers_list):
	for number in  numbers_list:
		print(f"dialing number {number}")


		"""


		client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            url=TWIML_INSTRUCTIONS_URL, method="GET")

        """

		time.sleep(5)



counter = 0
while counter < 3:
	dial_numbers(DIAL_NUMBER)
	counter+=1