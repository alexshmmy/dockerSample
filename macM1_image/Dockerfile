FROM --platform=linux/amd64 ubuntu:20.04

RUN apt-get update && apt-get install -y \
    wget \
    git \
    build-essential \
    nano

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -bfp /usr/opt/conda \
    && /usr/opt/conda/bin/conda init bash

ENV PATH /usr/opt/conda/bin:$PATH

RUN conda install -y python=3.7 \
    && conda update conda

# docker build . --tag ubu_test
# docker run -t -d --name ubutest ubu_test