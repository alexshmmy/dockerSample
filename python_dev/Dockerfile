# FROM python:3.6-slim-buster
FROM python:3.7-slim

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN apt-get update \
    && apt-get install -y wget

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3* -bfp /usr/opt/conda \
    && /usr/opt/conda/bin/conda init bash

ENV PATH /usr/opt/conda/bin:$PATH

COPY . .

# A cimpler one
# FROM python:3.6
# WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY . .

# Other commands
# RUN mkdir /project
# RUN cd /root/folder
# RUN git clone 

#FROM python:3.6

#WORKDIR /usr/src/app

#COPY requirements.txt ./

#RUN python -m pip install --upgrade pip \
#    && pip install --no-cache-dir -r requirements.txt

#COPY . .
