from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext

# Token bot
API_TOKEN = "8333327025:AAHoureGZR_7XbEWDVp7u92o24XayQuCZh0"

# Fungsi untuk memulai bot
async def start(update: Update, context: CallbackContext):
    # Membuat inline keyboard dengan tombol menuju mini app dan website
    keyboard = [
        [InlineKeyboardButton("Buka Mini App", web_app=WebAppInfo(url="https://dramabox-by-dracindo.vercel.app/"))],
        [InlineKeyboardButton("Buka Website", url="https://dracindo.site/")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Selamat datang! Klik tombol di bawah untuk mengakses Mini App dan Website Kami:', reply_markup=reply_markup)

# Setup bot dengan application
def main():
    application = Application.builder().token(API_TOKEN).build()
    
    # Menambahkan handler untuk /start
    application.add_handler(CommandHandler("start", start))
    
    # Menjalankan bot
    application.run_polling()

if __name__ == '__main__':
    main()
