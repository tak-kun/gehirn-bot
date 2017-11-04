# -*- coding: utf-8 -*-
import config
import telebot
import sys
from telebot import types
from datetime import datetime


bot = telebot.TeleBot(config.token)
online_flag = True

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    # bot.send_message(message.chat.id, message.text)
    # print(message.text)
    # str_time = datetime.now().strftime('%H:%M:%S')
    # bot.send_message(message.chat.id, str_time)
    # bot.send_message(message.chat.id, 'Привет, {name}. Рад тебя видеть.'.format(name=message.text))
    # keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # keyboard.add(*[types.KeyboardButton(name) for name in ['petuch', 'pidor']])
    # bot.send_message(message.chat.id, 'ТЫ КТО?',
    #     reply_markup=keyboard)

    #bot.send_message(message.chat.id, message.text)
    print(message.text)
    if message.text[0] == "/":
        print('command enabled')



if __name__ == '__main__':
     bot.polling(none_stop=online_flag)