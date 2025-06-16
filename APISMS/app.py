from twilio.rest import Client # importação para utilizar api de SMS

account_sid = '' # SID da conta Twilio
auth_token = '' # chave da API para usar API
twilio_number = '' # Número do Twilio que vai enviar a mensagem, pode ser comprado
destinatario = '+5511983699658' # numero que vai ser enviado deve ser registrado na API

mensagem = 'CALABOCA EDUARDO' # mensagem que quero enviar para esse numero através do SMS


client = Client(account_sid, auth_token) # utilizando o token pedido client para fazer o envio da mensagem
# Envia o sms
message = client.messages.create( # cria de fato o destino, o body é a mensagem que foi já realizada, qual numero veio esse sms e para onde
    body=mensagem,
    from_=twilio_number,
    to=destinatario
) 

 if message.sid == true :  # Verifica o SID da mensagem enviada, então se o numero SID da api como se fosse um token for válido ele envia 
     print(f'Mensagem enviada com SID: {message.sid}')
 else: 
     print("Falha em enviar o SMS, verifique os ID e token")


    
