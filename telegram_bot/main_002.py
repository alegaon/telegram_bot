from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# pass
your_token = "6417855773:AAGFdajhCARTXfVvKQaom469fkhsIFrZ_1M"

# Define a function to start the bot
def start(update: Update, context: CallbackContext):
    update.message.reply_text("Hello! I am your bot.")

# Define a function to save messages to a file
def save_message(update: Update, context: CallbackContext):
    message = update.message
    chat_id = message.chat_id
    message_text = message.text

    # Save the message to a file (append mode)
    with open(f'chat_{chat_id}_messages.txt', 'a', encoding='utf-8') as file:
        file.write(f"{message_text}\n")

def main():
    # Create an Updater instance with your bot token
    updater = Updater(token=your_token, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register a command handler
    dispatcher.add_handler(CommandHandler("start", start))

    # Register a message handler to save text messages
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, save_message))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
