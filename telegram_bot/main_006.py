# chat gtp

import requests

# Replace 'YOUR_BOT_TOKEN' with the token provided by BotFather.
BOT_TOKEN = '6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M'

# Define the base URL for the Telegram Bot API.
API_BASE_URL = f'https://api.telegram.org/bot{BOT_TOKEN}/'

# Send a message using the sendMessage method.
def send_message(chat_id, text):
    url = f'{API_BASE_URL}sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    response = requests.post(url, json=data)
    return response.json()

# Example: Sending a message to a chat with chat_id.
chat_id = '@tratarde'  # Replace with the actual chat ID.
message_text = 'Hello, this is your Telegram bot!'
send_message(chat_id, message_text)
