import telebot
from gpt import get_answer

bot = telebot.TeleBot("6927785010:AAGDZytTd-2JixpU5SxSxNTciX1JkTQlroI")

@bot.message_handler(commands=['gpt'])
def send_welcome(message):
    bot.reply_to(message, "Assalomu alaykum! NextGen IT Academy bot xizmatiga hush kelibsiz. Sizga qanday yordam bersam bo'ladi?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text[0] == "/":
        return
    if message.text:
        result = get_answer(message.text)
    bot.reply_to(message, result)

bot.polling()
