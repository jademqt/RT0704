FROM debian

MAINTAINER Jules_Jade

RUN apt update
RUN apt upgrade

RUN apt install -y python3-pip

RUN pip install Flask
RUN pip install requests

COPY * .

