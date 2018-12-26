FROM ubuntu:18.04

#ARG CACHEBUST

RUN apt-get update && apt-get install -y apt-utils sudo 


RUN adduser --disabled-password --gecos "snetservice user" netk && \
	adduser netk sudo && \
	echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER netk

#RUN whoami

RUN sudo apt-get install -y git \
	build-essential \
	python3.6 \
	python3.6-dev \
	python3-pip \
	wget \
	curl


WORKDIR /home/netk/

RUN curl https://bootstrap.pypa.io/get-pip.py | sudo python3.6

RUN pip --version

#RUN git clone https://github.com/singnet/network-analytics-services.git

RUN echo 2 && git clone https://github.com/edyirdaw/network-analytics-services.git

RUN cd network-analytics-services && git checkout --track origin/example_bipartition

RUN sudo pip install -r requirements.txt
	
