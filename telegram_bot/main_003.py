import os
import telebot 

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(command=['Greet'])
def greet(message):
    bot.reply_to(message, 'hey! Hows it going?')

bot.polling()
# 8.30min