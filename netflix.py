from telegram.ext import Updater, CommandHandler, MessageHandler

# Function to start the bot
def start(update, context):
    update.message.reply_text("Hello! Send me your Netflix email and password, and I'll check if it's correct.")

# Function to check Netflix credentials
def check_credentials(email, password):
    # Dummy function for now, replace with real API or checker logic.
    if email == "valid_email@example.com" and password == "validpassword":
        return True
    else:
        return False

# Handling messages manually without Filters
def handle_message(update, context):
    user_input = update.message.text
    try:
        # Assuming email and password are space-separated
        email, password = user_input.split()
        
        # Validate credentials
        if check_credentials(email, password):
            update.message.reply_text("✅ Correct credentials!")
        else:
            update.message.reply_text("❌ Wrong credentials. Try again!")
    except ValueError:
        # If input format is incorrect
        update.message.reply_text("❌ Please enter your email and password in the format: email password")

# Main function to set up the bot
def main():
    # Use your bot's token here
    updater = Updater("7550987469:AAEjXOHykyun6sv4YhNF2lLTz2NknF-G15U", use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register handlers without Filters
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(None, handle_message))  # Without Filters

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
