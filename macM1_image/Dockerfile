# A simple docker image with ubuntu 20.04 and conda for Mac M1
FROM --platform=linux/amd64 ubuntu:20.04

RUN apt-get update && \
    #apt-get upgrade -y && \
    apt-get install -y wget && \
    apt-get install -y git-lfs && \
    apt-get install -y build-essential && \
    apt-get install -y nano && \
    rm -rf /var/lib/apt/lists/*

RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
RUN bash ~/miniconda.sh -bfp /usr/opt/conda && \
    /usr/opt/conda/bin/conda init bash

ENV PATH /usr/opt/conda/bin:$PATH

RUN conda install -y python=3.8 \
    && conda update conda

RUN rm -rf /tmp/*


# How to build and run the Docker image:
# docker buildx ls
# docker buildx build --platform=linux/amd64 --tag ubu_test --file Dockerfile .
# docker run --platform=linux/amd64 -t -d --name ubutest ubu_test

# Old way:
# docker build --tag ubu_test --file Dockerfile .
# docker run -t -d --name ubutest ubu_test

# docker build . --tag ubu_test
# docker run -t -d --name ubutest ubu_test
