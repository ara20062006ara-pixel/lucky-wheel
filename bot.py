
import os
import telebot

TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🎡 أهلاً بك في ABODI WHEEL\n\nقريباً لعبة دولاب الحظ!"
    )

bot.infinity_polling()
