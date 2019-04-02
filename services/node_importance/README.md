[![SingnetLogo](docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

[![CircleCI](https://circleci.com/gh/singnet/network-analytics-services.svg?style=svg)](https://circleci.com/gh/singnet/network-analytics-services)

Given an input graph, the list of available servcies include:


* Finding set of nodes with the lowest eccentricity (center nodes)
* Finding set of nodes with the highest eccentricity (Peripheral/remote nodes)
* Finding the degree centrality of nodes
* Finding the closeness centrality of nodes
* Finding the betweeness centrality of nodes
* Finding the eigenvector centrality of nodes
* Finding the pagerank of nodes
* Finding the authorities and hubs of nodes using the hits algorithm

## User Guide

Please look at the [user guide](docs/USERGUIDE.md) for a detailed spec of the services and how to use the services.

## Running the service locally

### Install preprequisites

```
pip install -r requirements.txt
```


### Setup

Run the following commands to generate gRPC classes for Python

```
cd robustness
python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_node_importance/network_analytics_node_importance.proto
```

### Running unit tests

For testing the core functionalities
```
python3.6 test_node_importance.py
```

For testing the gRPC wrapper code
```
python3.6 test_snet_grpc_wrapper_node_importance.py
```

### Usage

To start the gRPC server locally

```
python3.6 snet_grpc_wrapper_node_importance.py