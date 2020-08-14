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

RUN echo 11

RUN mkdir /home/netk/pay/ \
    /home/netk/ssl/ \
    /home/netk/daemons/ \
    /home/netk/pay/bipartite_kovan/ \
    /home/netk/pay/robustness_kovan/ \
    /home/netk/pay/node_importance_kovan/ \
    /home/netk/pay/bipartite_ropsten/ \
    /home/netk/pay/robustness_ropsten/ \
    /home/netk/pay/node_importance_ropsten/ \
    /home/netk/pay/bipartite_mainnet/ \
    /home/netk/pay/robustness_mainnet/ \
    /home/netk/daemons/bipartite_kovan/ \
    /home/netk/daemons/robustness_kovan/ \
    /home/netk/daemons/node_importance_kovan/ \
    /home/netk/daemons/bipartite_ropsten/ \
    /home/netk/daemons/robustness_ropsten/ \
    /home/netk/daemons/node_importance_ropsten/ \
    /home/netk/daemons/bipartite_mainnet/ \
    /home/netk/daemons/robustness_mainnet/ \
    /home/netk/daemons/bipartite_mainnet_2/ \
    /home/netk/daemons/robustness_mainnet_2/ \
    /home/netk/dep

#ENV DAEMON_VERSION 1.0.0
#
#RUN wget -O snet-daemon.tar.gz https://github.com/singnet/snet-daemon/releases/download/v$DAEMON_VERSION/snet-daemon-v$DAEMON_VERSION-linux-amd64.tar.gz && \
#    tar  --strip-components=1 -xzf snet-daemon.tar.gz && \
#    cp snetd /home/netk/daemons/bipartite_kovan/ && \
#    cp snetd /home/netk/daemons/robustness_kovan/ && \
#    cp snetd /home/netk/daemons/node_importance_kovan/ && \
#    cp snetd /home/netk/daemons/bipartite_ropsten/ && \
#    cp snetd /home/netk/daemons/robustness_ropsten/ && \
#    cp snetd /home/netk/daemons/node_importance_ropsten/ && \
#    cp snetd /home/netk/daemons/bipartite_mainnet/ && \
#    cp snetd /home/netk/daemons/robustness_mainnet/ && \
#    rm -r snet-daemon.tar.gz && \
#    rm snetd

ENV DAEMON_VERSION_2 4.0.0

RUN wget -O snet-daemon.tar.gz https://github.com/singnet/snet-daemon/releases/download/v$DAEMON_VERSION_2/snet-daemon-v$DAEMON_VERSION_2-linux-amd64.tar.gz && \
    tar  --strip-components=1 -xzf snet-daemon.tar.gz && \
    cp snetd /home/netk/daemons/bipartite_mainnet_2/  && \
    cp snetd /home/netk/daemons/robustness_mainnet_2/


RUN echo 10

#COPY daemons/snetd_bipartite_kovan.json /home/netk/daemons/bipartite_kovan/
#COPY daemons/snetd_robustness_kovan.json /home/netk/daemons/robustness_kovan/
#COPY daemons/snetd_node_importance_kovan.json /home/netk/daemons/node_importance_kovan/
#COPY daemons/snetd_bipartite_ropsten.json /home/netk/daemons/bipartite_ropsten/
#COPY daemons/snetd_robustness_ropsten.json /home/netk/daemons/robustness_ropsten/
#COPY daemons/snetd_node_importance_ropsten.json /home/netk/daemons/node_importance_ropsten/
#COPY daemons/snetd_bipartite_mainnet.json /home/netk/daemons/bipartite_mainnet/
#COPY daemons/snetd_robustness_mainnet.json /home/netk/daemons/robustness_mainnet/
COPY daemons/snetd_bipartite_mainnet_2.json /home/netk/daemons/bipartite_mainnet_2/
COPY daemons/snetd_robustness_mainnet_2.json /home/netk/daemons/robustness_mainnet_2/
COPY supervisor/bipartite_grpc.conf /etc/supervisor/conf.d/
#COPY supervisor/bipartite_kovand.conf /etc/supervisor/conf.d/
#COPY supervisor/bipartite_ropstend.conf /etc/supervisor/conf.d/
#COPY supervisor/bipartite_mainnetd.conf /etc/supervisor/conf.d/
COPY supervisor/bipartite_mainnetd_2.conf /etc/supervisor/conf.d/
COPY supervisor/robustness_grpc.conf /etc/supervisor/conf.d/
#COPY supervisor/robustness_kovand.conf /etc/supervisor/conf.d/
#COPY supervisor/robustness_ropstend.conf /etc/supervisor/conf.d/
#COPY supervisor/robustness_mainnetd.conf /etc/supervisor/conf.d/
COPY supervisor/robustness_mainnetd_2.conf /etc/supervisor/conf.d/
COPY supervisor/node_importance_grpc.conf /etc/supervisor/conf.d/
#COPY supervisor/node_importance_kovand.conf /etc/supervisor/conf.d/
#COPY supervisor/node_importance_ropsten.conf /etc/supervisor/conf.d/


COPY supervisor/supervisord.conf /etc/supervisor/


WORKDIR /home/netk/dep

#RUN git clone https://github.com/singnet/network-analytics-services.git && \
#	cd network-analytics-services


# Needs to be uncommented for deploying. Comment out for circleci tests to pass.
'''
RUN whoami
RUN pwd

RUN echo 8 && \
	git clone https://github.com/edyirdaw/network-analytics-services.git && \
	cd network-analytics-services && \
	git checkout --track origin/example_bipartition

RUN cd network-analytics-services/services/bipartite && python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_bipartite/network_analytics_bipartite.proto
RUN cd network-analytics-services/services/robustness && python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_robustness/network_analytics_robustness.proto
RUN cd network-analytics-services/services/node_importance && python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_node_importance/network_analytics_node_importance.proto

WORKDIR /home/netk/network-analytics-services/services
'''
# Needs to be uncommented for deploying. Comment out for circleci tests to pass.
