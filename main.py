import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters

# Configure logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Telegram bot token
TOKEN = '6159975062:AAHL-Mhi6g5aPYOPmgvywDEvZuGCt5c_hMw'

# Command handler for the start command
def start(update: Update, context: CallbackContext) -> None:
    """Send a welcome message when the command /start is issued."""
    update.message.reply_text('Welcome! Send me a Telegram file to generate a streaming link.')

# Command handler for file message
def file_message(update: Update, context: CallbackContext) -> None:
    """Handle incoming file message."""
    file = update.message.document  # Get the received file object
    file_id = file.file_id  # Get the file ID

    # Generate streaming link
    streaming_link = context.bot.get_file(file_id).file_path

    # Share the streaming link
    update.message.reply_text(f"Streaming link: {streaming_link}")

# Main function
def main() -> None:
    """Run the bot."""
    # Create the Updater and pass it the bot token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.document, file_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C
    updater.idle()

if __name__ == '__main__':
    main()
