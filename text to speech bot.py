import telebot
from gtts import gTTS
import os

# توکن ربات تلگرامی خود را در این قسمت قرار دهید
TOKEN = '7125457464:AAHe2xzq2ee1AyQvussrpLWYXOr5XJus4JM'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "سلام! برای تبدیل متن به صدا، متن خود را ارسال کنید.")

@bot.message_handler(func=lambda message: True)
def convert_text_to_speech(message):
    text = message.text
    tts = gTTS(text, lang='en')
    tts.save("output.mp3")
    audio = open("output.mp3", 'rb')
    bot.send_audio(message.chat.id, audio)
    os.remove("output.mp3")

bot.polling()