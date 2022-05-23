FROM python:3.7

RUN apt update -y && apt upgrade -y 

RUN apt install  -y unixodbc unixodbc-dev

RUN pip3 install --upgrade pip

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

WORKDIR /work