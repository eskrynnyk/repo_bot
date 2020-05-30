import telebot
import config # подключаем конфиг, чтобы взять с него токен бота

bot = telebot.TeleBot('1136026078:AAHYkWNwfDiXtzzdShyHQ8EB2tkvFZxwzCM')
print(bot.get_me())