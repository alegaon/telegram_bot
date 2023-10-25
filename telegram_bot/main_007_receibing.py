from flask import Flask, request
import telebot

BOT_TOKEN = '6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M'


app = Flask(__name__)

# Initialize your bot
bot = telebot.TeleBot(BOT_TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = telebot.types.Update.de_json(json_str)
    # Process the update (e.g., respond to the user)
    # Use the 'update' object to handle incoming messages, commands, etc.
    return ''

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8443, ssl_context=('cert.pem', 'key.pem'))
