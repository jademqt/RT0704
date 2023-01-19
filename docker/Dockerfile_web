FROM debian

LABEL MAINTAINER Jules_Jade

RUN apt update
RUN apt upgrade -y

RUN apt install -y python3-pip

RUN pip install Flask
RUN pip install requests

RUN mkdir -p /home/app
WORKDIR /home/app

RUN mkdir /home/app/rest
COPY rest /home/app/rest

RUN mkdir /home/app/web
COPY web /home/app/web

COPY run.sh /home/app
COPY config.json /home/app

