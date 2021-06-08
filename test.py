import os

from flask import Flask, request
import requests
import telebot

TOKEN = "1895688998:AAE7j7nSXQm8dZ942zT4OUcKKqXXY4w_frk"
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)
r = requests.get('https://baf-backend.azurewebsites.net/spot/get-open-position?BaseCurrency=DODO&QuoteCurrency=USDT')    


@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, 'Hello, ' + message.from_user.first_name)


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    bot.reply_to(message, message.text)

@bot.message_handler(commands=['getpos'])
def getpos(message):
    bot.reply_to(message, r.text)



@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://aqueous-headland-18855.herokuapp.com/' + TOKEN)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

