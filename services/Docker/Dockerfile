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


RUN sudo apt-get install -y supervisor && \
    sudo rm /etc/supervisor/supervisord.conf

##Not used for now
#RUN sudo mkdir /var/log/bipartite_kovan/ \
#    /var/log/bipartite_ropsten/ \
#    /var/log/robustness_kovan/ \
#    /var/log/robustness_ropsten/


RUN mkdir /home/top/pay/ \
    /home/top/daemons/ \
    /home/top/pay/bipartite_kovan/ \
    /home/top/pay/robustness_kovan/ \
    /home/top/pay/bipartite_ropsten/ \
    /home/top/pay/robustness_ropsten/ \
    /home/top/daemons/bipartite_kovan/ \
    /home/top/daemons/robustness_kovan/ \
    /home/top/daemons/bipartite_ropsten/ \
    /home/top/daemons/robustness_ropsten/

ENV DAEMON_VERSION 0.1.6

RUN wget -O snet-daemon.tar.gz https://github.com/singnet/snet-daemon/releases/download/v$DAEMON_VERSION/snet-daemon-v$DAEMON_VERSION-linux-amd64.tar.gz && \
    tar  --strip-components=1 -xzf snet-daemon.tar.gz && \
    cp snetd /home/top/daemons/bipartite_kovan/ && \
    cp snetd /home/top/daemons/robustness_kovan/ && \
    cp snetd /home/top/daemons/bipartite_ropsten/ && \
    cp snetd /home/top/daemons/robustness_ropsten/


RUN echo 1

COPY daemons/snetd_bipartite_kovan.json /home/top/daemons/bipartite_kovan/
COPY daemons/snetd_robustness_kovan.json /home/top/daemons/robustness_kovan/
COPY daemons/snetd_bipartite_ropsten.json /home/top/daemons/bipartite_ropsten/
COPY daemons/snetd_robustness_ropsten.json /home/top/daemons/robustness_ropsten/
COPY supervisor/bipartite_grpc.conf /etc/supervisor/conf.d/
COPY supervisor/bipartite_kovand.conf /etc/supervisor/conf.d/
COPY supervisor/bipartite_ropsten.conf /etc/supervisor/conf.d/
COPY supervisor/robustness_grpc.conf /etc/supervisor/conf.d/
COPY supervisor/robustness_kovand.conf /etc/supervisor/conf.d/
COPY supervisor/robustness_ropsten.conf /etc/supervisor/conf.d/
COPY supervisor/supervisord.conf /etc/supervisor/


WORKDIR /home/netk/dep

#RUN git clone https://github.com/singnet/network-analytics-services.git && \
#	cd network-analytics-services

#RUN echo 8 && \
#	git clone https://github.com/edyirdaw/network-analytics-services.git && \
#	cd network-analytics-services && \
#	git checkout --track origin/example_bipartition

#RUN pwd

#RUN cd network-analytics-services/services/bipartite && python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_bipartite/network_analytics_bipartite.proto
#RUN cd network-analytics-services/services/robustness && python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_bipartite/network_analytics_robustness.proto

#WORKDIR /home/netk/network-analytics-services/services

