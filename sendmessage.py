from twilio.rest import Client 
 
account_sid = 'AC3945ce9a7757ce62d369f0d8e874fb8e' 
auth_token = '28053d20f98dbe9b397d6d9128ceb1d9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='+15104220854',  
                              body='Bro send me the bro',      
                              to='+34655701689' 
                          ) 
 
print(message.sid)