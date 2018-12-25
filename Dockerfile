FROM ubuntu:18.04

RUN apt-get update && apt-get install -y sudo \
	git \
	build-essential \
	python3.6 \
	python3.6-dev \
	python3-pip \
	wget \
	curl

RUN adduser --disabled-password --gecos "snetservice user" netk && \
	adduser netk sudo && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers && \
	su netk

WORKDIR /home/netk/

RUN git clone https://github.com/singnet/network-analytics-services.git

RUN curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6

RUN pip --version

RUN sudo pip install -r requirements.txt
	
