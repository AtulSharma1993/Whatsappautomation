from twilio.rest import Client

account_sid = 'AC96091bf0ac677d79659f09653ccabed3'
auth_token = '1566cdfe9f9a257a1bb33dc140f80409'
client = Client(account_sid, auth_token)
def send_text() :
 message = client.messages.create(
    from_='whatsapp:+14155238886',
        body='Never stop grinding!!!!',
    to='whatsapp:+919988998828'
    )

 print(message.sid)