import telebot
from telebot import types
import random

chars = "+-*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"



bot = telebot.TeleBot('6297796941:AAHFY4aPqhb5_8K07njP1_9bu5gRn_mLbOM')



@bot.message_handler(commands=['start'])
def start(message):
    startbut = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton(text='Привет👋')
    startbut.add(btn1)
    bot.send_message(message.chat.id, "Привет здесь ты можешь создавать пароли👋",reply_markup=startbut)


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == 'Привет👋':
        mainbut = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='Создать пароль🛠')
        mainbut.add(btn1)
        bot.send_message(message.chat.id, "Нажми", reply_markup=mainbut)


    elif message.text == 'Создать пароль🛠':
        createbut = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton(text='6 символов⚪️')
        btn2 = types.KeyboardButton(text='10 символов⚫️')
        btn3 = types.KeyboardButton(text='14 символов🔴')
        createbut.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, "Выбери длину пароля ", reply_markup=createbut)

    elif message.text == '6 символов⚪️':
        password = ''
        length = 6
        for i in range(length):
            password += random.choice(chars)
        bot.send_message(message.chat.id,f"Твой пароль: {password}")

    elif message.text == '10 символов⚫️':
        password = ''
        length = 10
        for i in range(length):
            password += random.choice(chars)
        bot.send_message(message.chat.id,f"Твой пароль: {password}")

    elif message.text == '14 символов🔴':
        password = ''
        length = 14
        for i in range(length):
            password += random.choice(chars)
        bot.send_message(message.chat.id,f"Твой пароль: {password}")

bot.polling()