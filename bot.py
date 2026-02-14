from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN = 8333327025:AAHoureGZR_7XbEWDVp7u92o24XayQuCZh0

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Halo, saya bot Telegram!')

def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Perintah yang tersedia:\n/start - Memulai bot\n/help - Menampilkan daftar perintah')

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()