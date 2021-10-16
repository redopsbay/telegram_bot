# Telegram Bot #

![Telegram Bot](https://telegram.org/img/t_logo_2x.png)

## Overview

This is useful for micro services application for job controller or system daemon to generate alert's and notifications. Additionally for scripting, Automation and CI/CD Pipelines



## Requirements ##

- [telegram bot](https://github.com/python-telegram-bot/python-telegram-bot)
- [Python3.6+](https://python.org)

## Installation 
```
root@ubuntu-focal:/telegram_bot# sudo apt install python3-pip && sudo pip3 install python-telegram-bot
```

## Running the script ##
```
root@ubuntu-focal:/telegram_bot# export TELEGRAM_TOKEN="telegram_token"
root@ubuntu-focal:/telegram_bot# export TELEGRAM_CHATID=chat_id
root@ubuntu-focal:/telegram_bot# export TELEGRAM_MESSAGE="telegram_text"
root@ubuntu-focal:/telegram_bot# python3 main.py
```


## Using Docker Telegram Bot ##

### Building the container
```
root@ubuntu-focal:/telegram_bot# docker build -t telbot_client:v1 . 
```

### Running the container
```
root@ubuntu-focal:/telegram_bot# docker run --rm --hostname telegram_bot --name telegram_bot --env TELEGRAM_TOKEN='YOUR_TELEGRAM_TOKEN' --env TELEGRAM_CHATID='YOUR_TELEGRAM_CHATID' --env TELEGRAM_MESSAGE="Trigger: error_rate_too_high" telbot:v1
```