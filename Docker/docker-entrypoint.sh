#!/bin/bash

if [[ -d '/opt/telegram_bot' ]]
then
    if [[ -f '/opt/telegram_bot/main.py' ]]
    then
        /usr/bin/python3 /opt/telegram_bot/main.py
        exit 0
    fi
fi

