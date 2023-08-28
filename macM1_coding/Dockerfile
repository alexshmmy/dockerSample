# A simple docker image with Ubuntu 20.04
# conda for Python, C, C++, Java, Julia and Javascript 
# dependencies for development in Mac M1
#
# Run with:
# docker buildx build --platform=linux/amd64 --tag ubu_test --file Dockerfile .
# docker run --platform=linux/amd64 -t -d --name ubutest ubu_test

FROM --platform=linux/amd64 ubuntu:20.04

# needed for Java installation
ARG DEBIAN_FRONTEND=noninteractive

# Install wget, git, nano, gcc etc.
RUN apt-get update && \
    apt-get install -y wget && \
    apt-get install -y git-lfs && \
    apt-get install -y build-essential && \
    apt-get install -y nano

# Install Java dependencies
# RUN add-apt-repository ppa:openjdk-r/ppa
RUN apt-get update && \
    apt-get install -y openjdk-11-jdk-headless

# Set the Java Home environment variable
ENV JAVA_HOME /usr/lib/jvm/java-11-openjdk-amd64/
RUN export JAVA_HOME

# Reduce the size of Docker image
RUN rm -rf /var/lib/apt/lists/*

# Remove cached package files
RUN apt-get clean 

# RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda.sh
# RUN bash ~/miniconda.sh -bfp /usr/opt/conda && \
#     /usr/opt/conda/bin/conda init bash

# ENV PATH /usr/opt/conda/bin:$PATH

# RUN conda install -y python=3.8 \
#     && conda update conda

RUN rm -rf /tmp/*