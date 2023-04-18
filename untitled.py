import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Define a function to handle the /start command
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Hello! Send me a file and I'll store it for you.")

# Define a function to handle file messages
def file_handler(update, context):
    file = update.message.document
    file_name = file.file_name
    file_id = file.file_id
    file_path = f"{file_id}_{file_name}"
    file_path = os.path.join("path/to/directory", file_path)
    file.download(custom_path=file_path)
    context.bot.send_message(chat_id=update.message.chat_id, text=f"File '{file_name}' has been stored.")

# Define a function to handle unknown commands
def unknown(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Sorry, I didn't understand that command.")

# Set up the bot
TOKEN = 'your_bot_token_here'
bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)

# Set up command handlers
start_handler = CommandHandler('start', start)
updater.dispatcher.add_handler(start_handler)

# Set up message handlers
file_handler = MessageHandler(Filters.document, file_handler)
updater.dispatcher.add_handler(file_handler)

# Set up unknown command handler
unknown_handler = MessageHandler(Filters.command, unknown)
updater.dispatcher.add_handler(unknown_handler)

# Start the bot
updater.start_polling()
updater.idle()
