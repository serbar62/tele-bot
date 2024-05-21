import os
# from background import keep_alive  #импорт функции для поддержки работоспособности
# import pip

# pip.main(['install', 'pytelegrambotapi'])
import telebot
import time

import telebot
from telebot import types

bot = telebot.TeleBot('6701765680:AAFrEjwUvuta-u18ckiz1hadOvrPvAqqH10')

#   CHAT_ID = -1002120996109
#   USER_ID = 899527476
#  '@vygodnoe_strahovanie'    https://t.me/asiaa_travel
#   callback.message.from_user.id


@bot.message_handler(func=lambda msg: msg.text == 'photo')
@bot.message_handler(commands=["start"])
def start(message: types.Message):

    mess = (
        f'<b>Привет, {message.from_user.first_name}!</b>\n\n<b>Получите Ваш подарок</b> - книгу, которая станет Вашим надёжным путеводителем в мире путешествий и подробным справочником онлайн сервисов!\n\nЧтобы получить <b>книгу-инструкцию</b> по подготовке и организации отдыха в путешестивях, нажмите кнопку <b>Подписаться</b>'
        f'\n\nЕсли Вы уже подписаны, жмите кнопку <b>Получить книгу</b>')

    markup = types.InlineKeyboardMarkup()
    podpisats = types.InlineKeyboardButton('Подписаться \U0001F449',
                                           callback_data='yes',
                                           url='https://t.me/asiaa_travel')
    podpisan = types.InlineKeyboardButton('Получить книгу', callback_data='no')
    markup.add(podpisats, podpisan)

    bot.send_photo(
        message.chat.id,
        "https://vladenie-21.ru/wp-content/uploads/2024/05/Ded-1.jpg",
        caption=mess,
        reply_markup=markup,
        parse_mode='HTML')


@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):

    mess2 = (
        f'<b>{callback.message.from_user.first_name},</b>\n\nУ Вас не получилось подписаться на наш канал?'
        f'\n\nПопробуйте ещё раз. Нажмите кнопку <b>Подписаться</b>, Вы попадёте в наш канал. Подпишитесь на канал, а затем вернитесь обратно ко мне и нажмите кнопку <b>Получить книгу</b>'
    )

    mess3 = (
        f'<b>Благодарю Вас за подписку на наш Telegram канал!</b>\nНадеюсь Вам будет интерсено!\n\nЧтобы получить книгу-инструкцию - ваш надёжный путеводитель в мире путешествий и подробный справочник онлайн сервисов, перейдите по ссылке  \n  \U0001F449'
        f'https://vladenie-21.ru/podar_Yr34.php')

    markup = types.InlineKeyboardMarkup()
    podpisats = types.InlineKeyboardButton('Подписаться \U0001F449',
                                           callback_data='yes',
                                           url='https://t.me/asiaa_travel')
    podpisan = types.InlineKeyboardButton('Получить книгу', callback_data='no')
    markup.add(podpisats, podpisan)

    if callback.data == 'no':
        try:
            res = bot.get_chat_member(chat_id='@asiaa_travel',
                                      user_id=callback.message.from_user.id)
            if res.status == 'member' or 'creator':
                bot.send_message(callback.message.chat.id,
                                 text=mess3,
                                 parse_mode='HTML')

        except:
            bot.send_message(callback.message.chat.id,
                             text=mess2,
                             reply_markup=markup,
                             parse_mode='HTML')


# keep_alive()
if __name__ == '__main__':
    bot.polling(none_stop=True)
