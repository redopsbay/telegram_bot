FROM ubuntu:focal-20210921

RUN apt-get -y update && apt-get install -y python3-pip && pip3 install python-telegram-bot tzdata

ADD docker-entrypoint.sh /usr/local/bin/docker-entrypoint.sh

RUN mkdir /opt/telegram_bot && chown 0777 -R /opt/telegram_bot

ADD main.py /opt/telegram_bot/

RUN chmod +x /opt/telegram_bot/main.py && chown 0777 /opt/telegram_bot/main.py

RUN chmod +x /usr/local/bin/docker-entrypoint.sh 

ENV TELEGRAM_TOKEN=''
ENV TELEGRAM_MESSAGE=''
ENV TELEGRAM_CHATID=''

ENTRYPOINT ["docker-entrypoint.sh"]