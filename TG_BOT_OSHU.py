# 5389008971:AAE4aS23O3iVE7_mfiARYJlyKi3HyuajZVg

import telebot
import requests
from bs4 import BeautifulSoup as b
import random

token = '5389008971:AAE4aS23O3iVE7_mfiARYJlyKi3HyuajZVg'
bot = telebot.TeleBot(token)

url = 'https://citaty.info/topic/samorazvitie-i-samosovershenstvovanie?page=5'

r = requests.get(url)

bot.polling(none_stop = True)

soup_page = b(r.text, 'html.parser')

wisdomes = soup_page.find_all('div', class_='field-item even last')

alone_wisdomes = []
for i in wisdomes:
    alone_wisdomes.append(i.text)


@bot.message_handler()
def get_wisdom(message):
    if message.text == 'мудрость' or message.text == 'Мудрость':
        bot.send_message(message.chat.id, random.choice(alone_wisdomes))
    else:
        bot.send_message(message.chat.id, 'Похоже, Вы ошиблись адресом, здесь можно только обрести знание')


bot.polling(none_stop = True)
