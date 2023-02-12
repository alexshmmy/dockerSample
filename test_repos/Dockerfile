# FROM python:3.6-slim-buster
FROM python:3.8

# install git-lfs
RUN apt-get update && apt-get install -y git-lfs

# update pip
RUN pip install --upgrade "pip == 22.2"

# download the repo you want to test
RUN chmod 777 /root
RUN cd /root && git clone https://github.com/alexshmmy/dockerSample.git

############## commands inside dockerfile
# chmod 755 /root (or 777 /root)
# curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# source .profile 
# add export PATH="$PATH:/root/marl/bin" in .cache/pypoetry/bin/activate
# source activate

# Build the image
#docker build . --tag test_repo

# Run the image 
#docker run -t -d --name testrepo test_repo

# The names python_app and python_dev are the names of the image and container respectively and can be changed.

# docker stop python_dev
# docker restart python_dev
# docker start python_dev
# docker container ls -a
# docker container rm CONT_ID
# docker image ls
# docker image rm CONT_ID