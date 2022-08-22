import telebot
from telebot import types
import time

bot = telebot.TeleBot('5401702475:AAHKBwN-MjZ13RTnXmy3uhz_SQC3Nt2pz8g')



m = 0
tmp_yes = 1
s = 0
min_sec_format = ''
num_of_secs = 0
tmp_no = 0

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.from_user.id, "name work")
    bot.register_next_step_handler(message, get_name)


def get_name(message):
    global name
    name = message.text
    if message.text == '/start':
        bot.register_next_step_handler(message, get_name)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn_start = types.KeyboardButton("начинать")
        markup.add(btn_start)
        bot.send_message(message.chat.id, text="trebovaniye: ", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def location(message):
    if message.text == "начинать" or message.text == "no":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("otmen")
        btn2 = types.KeyboardButton("look time")
        btn3 = types.KeyboardButton("pause")
        markup.add(btn1, btn2)
        markup.add(btn3)
        bot.send_message(message.chat.id, text="не отвлекайтесь!", reply_markup=markup)
        bot.register_next_step_handler(message, intput_func)

        if tmp_no == 0:
            global m, s, min_sec_format, num_of_secs
            num_of_secs = 20
            global tmp_yes
        while num_of_secs:
            m, s = divmod(num_of_secs, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(type(min_sec_format))
            print(min_sec_format)
            time.sleep(1)
            num_of_secs -= 1
            if tmp_yes == 0:
                break
        if num_of_secs == 0:
            print('Countdown finished.')
            bot.send_message(message.from_user.id, "Pomidor finished")
            tmp_yes = 1
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_start = types.KeyboardButton("начинать")
            markup.add(btn_start)
            bot.send_message(message.chat.id, text="trebovaniye: ", reply_markup=markup)
            bot.register_next_step_handler(message, location)
        else:
            num_of_secs = 20
            tmp_yes = 1


def intput_func(message):
    if message.text == "otmen":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn11 = types.KeyboardButton("yes")
        btn21 = types.KeyboardButton("no")
        markup.add(btn11, btn21)
        bot.send_message(message.chat.id, text="anniqmi?", reply_markup=markup)
        bot.register_next_step_handler(message, func_otmen)
    elif message.text == "look time":
        bot.send_message(message.from_user.id, min_sec_format)
        bot.register_next_step_handler(message, intput_func)
    elif message.text == "pause":
        pass
    else:
        return "0"

def func_otmen(message):
    if message.text == "yes":
        get_name(message)
        global tmp
        tmp = 0
    elif message.text == "no":
        print("asfdsfjd")
        global tmp_no
        tmp_no = 1
        location(message)


bot.polling(none_stop=True)



