# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot.types import Message
import parsing as p
TOKEN = '1062192421:AAF6rpH-ZNf-tv53N-bNCNsF0EXKw3cjLOw'
#chat_id = '719274325'
bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(commands=['how are you'])
reply = p.get_main_tennis()
reply1 = p.get_main_football()


@bot.message_handler(commands=['start','начать','ready'])
def send_welcome(message):
    bot.send_message(
        message.chat.id,
        '''Добро пожаловать к нам в бот
        ''',
        reply_markup = keyboard())
@bot.message_handler(content_types=["text"])
def send_anything(message):
    chat_id = message.chat.id
    if message.text == '🏓 Теннис':
        text = '✅ Вот список ближайших мачтов по теннису \n\n'
        bot.send_message(chat_id, text)
        for i in range(len(reply)):
            bot.send_message(chat_id, ' в {}  ::::::::  {} 🆚 {} '.format(reply[i][0], reply[i][1], reply[i][4]), reply_markup=keyboard())
    elif message.text == '⚽ Футбол':
        text = '✅ Вот список ближайших мачтов по футболу \n\n'
        text1 = '✅ Вот список 10 ближайших мачтов по футболу \n\n'
        if len(reply1)>=10:
            bot.send_message(chat_id,text1)
            for i in range(10):
                bot.send_message(chat_id,'{}  ДАТА: {} в {} :::::: {} 🆚 {}'.format(reply1[i][4], reply1[i][2], reply1[i][3],reply1[i][0], reply1[i][1],reply_markup=keyboard()))
        else:
            bot.send_message(chat_id,text)
            for i in range(len(reply1)):
                bot.send_message(chat_id, '{}  ДАТА: {} в {}:::::: {} 🆚 {}'.format(reply1[i][4],reply1[i][2],reply1[i][3],reply1[i][0],reply1[i][1], reply_markup = keyboard()))
    elif message.text == '/stop':
        bot.send_message(chat_id, 'Бот остановлен 🌝 🌝 🌝')
        bot.stop_polling()

def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('🏓 Теннис')
    btn2 = types.KeyboardButton('⚽ Футбол')
    markup.add(btn1,btn2)
    return markup

bot.polling()