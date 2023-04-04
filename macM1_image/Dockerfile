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

######################################################
# Other docker image:
# FROM nvidia/cuda:11.5.1-cudnn8-runtime-ubuntu20.04

# RUN apt-get update && \
#     #apt-get install -y python3-pip
#     apt-get upgrade -y && \
#     # install python3.7
#     apt install -y software-properties-common && \
#     add-apt-repository -y ppa:deadsnakes/ppa && \
#     apt-get update && \
#     apt-get install -y python3.7 && \
#     apt-get install -y python3-pip

# RUN pip install --no-cache-dir --upgrade pip && \
#     pip install --no-cache-dir "pandas<=1.3.5" && \
#     pip install --no-cache-dir "numpy<=1.19.5" && \
#     pip install --no-cache-dir "matplotlib<=3.5" && \
#     pip install --no-cache-dir "tensorflow<=2.10.0rc0"

# RUN chmod 777 /root

# docker build . --tag tens_ubnvidia
# docker run -t -d --name tensubunvidia tens_ubnvidia
