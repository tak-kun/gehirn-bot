# -*- coding: utf-8 -*-
import config
import telebot
import sys
import os
import time

#from sh import ping
from telebot import types
from datetime import datetime


bot = telebot.TeleBot(config.token)
online_flag = True

@bot.message_handler(content_types=["text"])
def response(message): # Название функции не играет никакой роли, в принципе
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
    message_data = message.text
    message_data = message_data.split()
    if message_data[0] == "/ping":
        print('ping command enabled')
        try:
            hostname = message_data[1]
            response = os.system('ping -c 1 ' + hostname)
            if response == 0:
                bot.send_message(message.chat.id, 'Hostname is online!')
            else:
                bot.send_message(message.chat.id, 'Hostname is not available')
        except:
            bot.send_message(message.chat.id, 'Error ping')
    elif message_data[0] == "/temp":
        try:
            if message_data[1] == 'proc':
                response = os.popen('vcgencmd measure_temp').readline()
                response = response.replace("temp=","").replace("'C\n","")
                bot.send_message(message.chat.id, response)
                print(response)
        except:
            bot.send_message(message.chat.id, 'error temp')

    elif message_data[0] == '/help':
            response = "/ping _name_; /temp _name_;"
            bot.send_message(message.chat.id, response)

    elif message_data[0] == 'Привет':
            response = "Hi, tak-kun! 😍"
            bot.send_message(message.chat.id, response)

    elif message_data[0] == "/poweroff":
            bot.send_message(message.chat.id, "Good bye! 😌")
            response = os.system('sudo poweroff')


if __name__ == '__main__':
     bot.polling(none_stop=online_flag)