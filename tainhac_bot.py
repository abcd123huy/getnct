import sys
import time
import telepot
from telepot.loop import MessageLoop
from mtranslate import translate
import json
import requests

def handle(msg):a
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        if msg['text'].find('@nct')>-1:
            linknct = msg['text'].split(" ",1)[1]
            data = [('url', linknct),]
            r = requests.post('http://dekcp.design/flat/getnct/index.php', data=data)
            bot.sendMessage(chat_id=chat_id, text='Status: %s' % r.json()[0]['msg'])
            bot.sendMessage(chat_id=chat_id, text='Singer: %s' % r.json()[0]['casy'])
            bot.sendMessage(chat_id=chat_id, text='Song: %s' % r.json()[0]['baihat'])
            bot.sendMessage(chat_id=chat_id, text='128: %s' % r.json()[0]['128'])
            bot.sendMessage(chat_id=chat_id, text='320: %s' % r.json()[0]['320'])
            bot.sendMessage(chat_id=chat_id, text='Lossless: %s' % r.json()[0]['lossless'])
        else:
            bot.sendMessage(chat_id=chat_id, text=translate(msg['text'], 'vi'))

TOKEN = '382982178:AAF-ybrUiJ1Pm7hckUUFoqTvNH6sBFEvvFM'  # get token from command-line

bot = telepot.Bot(TOKEN)
bot.setWebhook()
MessageLoop(bot, handle).run_as_thread()
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
