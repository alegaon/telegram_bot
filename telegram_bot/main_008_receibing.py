import telebot
import ipdb 

BOT_TOKEN = '6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M'


# Initialize your bot
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Handle the received message
    chat_id = message.chat.id
    text = message.text
    
    print(text)
    bot.send_message(chat_id, f"esto lo dijiste vos pararulo: {text}")

# Start polling for updates
bot.polling()
