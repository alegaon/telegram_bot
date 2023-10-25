import telebot
import logging

YOUR_BOT_TOKEN = "6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M"

# Set up logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Initialize your bot
bot = telebot.TeleBot(YOUR_BOT_TOKEN)

# Define a function to save messages to a file
@bot.message_handler(func=lambda message: True)
def save_message(message):
    chat_id = message.chat.id
    message_text = message.text

    # Save the message to a file (append mode)
    with open(f'chat_{chat_id}_messages.txt', 'a', encoding='utf-8') as file:
        file.write(f"{message_text}\n")

# Start the bot
bot.polling(none_stop=True)
