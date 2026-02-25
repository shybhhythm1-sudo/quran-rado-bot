from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# 🔴 حط توكن البوت هنا
BOT_TOKEN = "8008103594:AAGk4hcB96TbVIwzw_JmPijiTrAtej38nic"

# 📻 إذاعة القرآن الكريم من القاهرة (رابط مباشر شغال)
QURAN_RADIO_URL = "https://stream.radiojar.com/8s5u5tpdtwzuv"

def start(update: Update, context: CallbackContext):
    keyboard = [
        [
            InlineKeyboardButton(
                "📻 تشغيل إذاعة القرآن الكريم",
                url=QURAN_RADIO_URL
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text(
        "🕌 مرحبًا بك في بوت إذاعة القرآن الكريم\n"
        "اضغط على الزر لتشغيل الإذاعة المباشرة من القاهرة",
        reply_markup=reply_markup
    )

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
