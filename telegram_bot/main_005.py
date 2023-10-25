# link
# https://www.youtube.com/watch?v=i-8KwhmAh8c&t=328s&ab_channel=SySCursos

# https:/api.telegram.org/
# https:/core.telegram.org/bots/api


import requests


# message_id
requests.post(
    'https://api.telegram.org/bot6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M/message_id',
    data = {'chat_id' : '@tratarde',
            'text' : 'alo, que talga, 005',}
            )
print('tomar mensajes')

requests.post(
    'https://api.telegram.org/bot6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M/sendMessage',
    data = {'chat_id' : '@tratarde',
            'text' : 'alo, que talga, 005',}
            )
print('sendMessage')