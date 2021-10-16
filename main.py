#!/usr/bin/python3

import os
import sys
import time
import datetime
import json

try:
    import telegram
except ImportError:
    print("[ERROR] Failed to import telegram module.")
    exit(-1)

def init_telegram(token=''):
    '''
        @ Initialized telegram object
    '''
    if token is None or token == '':
        print("[ERROR] Telegram bot token should be provided")
        exit(-1)
    bot = telegram.Bot(token=token)
    return bot

def send_msg(bot=None, Message="", ChatID=""):
    '''
        @ Create text message 
        bot: Bot Object (telegram.Bot)
        Message: Text Message
        ChatID: Chat ID to specify the group chat id.
    '''
    if bot is None:
        print("[ERROR] Bot object should be specified")
        exit(-1)
    telegram_bot = bot
    telegram_bot.send_message(text="Received Time: " + str(datetime.datetime.now()) + "\n\n\n" + Message, chat_id=ChatID)

def main():
    '''
        @ Main Function
    '''
    TOKEN = os.getenv('TELEGRAM_TOKEN') # None
    MESSAGE = os.getenv('TELEGRAM_MESSAGE')
    CHATID = os.getenv('TELEGRAM_CHATID')

    if TOKEN is None or TOKEN == '':
        print("[ERROR] Environment variable `TOKEN` must be specified!")
        exit(-1)
    if MESSAGE is None or MESSAGE == '':
        print("[ERROR] Environment variable `MESSAGE` must be specified!")
        exit(-1)
    if CHATID is None or CHATID == '':
        print("[ERROR] Environment variable `CHATID` must be specified!")
        exit(-1)

    bot_handler = init_telegram(TOKEN)
    send_msg(bot=bot_handler,Message=MESSAGE,ChatID=CHATID)

if __name__ == '__main__':
    main()