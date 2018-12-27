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


WORKDIR /tmp

COPY requirements.txt /tmp/
RUN sudo pip install -r requirements.txt
RUN echo 1
COPY requirements_2.txt /tmp/
RUN sudo pip install -r requirements_2.txt

WORKDIR /home/netk/

#RUN git clone https://github.com/singnet/network-analytics-services.git && \
#	cd network-analytics-services

#RUN echo 8 && \
#	git clone https://github.com/edyirdaw/network-analytics-services.git && \
#	cd network-analytics-services && \
#	git checkout --track origin/example_bipartition

#RUN pwd

#RUN cd network-analytics-services/services && python3.6 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. network_analytics.proto

#WORKDIR /home/netk/network-analytics-services/services

