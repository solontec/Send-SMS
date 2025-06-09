from twilio.rest import Client


account_sid = '' # SID da conta Twilio
auth_token = '' # chave da API para utilização do Twilio
twilio_number = '' # Número do Twilio que vai enviar a mensagem


destinatario = '+5511983699658'

# Mensagem
mensagem = 'CALABOCA EDUARDO'

# Cliente Twilio
client = Client(account_sid, auth_token)

# Envio do SMS
message = client.messages.create(
    body=mensagem,
    from_=twilio_number,
    to=destinatario
)

# Verifica o SID da mensagem enviada
print(f'Mensagem enviada com SID: {message.sid}')
