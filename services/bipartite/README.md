[![SingnetLogo](docs/assets/singnet-logo.jpg?raw=true 'SingularityNET')](https://singularitynet.io/)

[![CircleCI](https://circleci.com/gh/singnet/network-analytics-services.svg?style=svg)](https://circleci.com/gh/singnet/network-analytics-services)

The list of available servcies includes:

* Bipartite graph construction
* Bipartite graph projection



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
cd bipartite
python3.6 -m grpc_tools.protoc -I. --python_out=.  --grpc_python_out=. service_spec_bipartite/network_analytics_bipartite.proto
```



### Running unit tests

For testing the core functionalities
```
python3.6 test_bipartite_graphs.py
```

For testing the gRPC wrapper code
```
python3.6 test_snet_grpc_wrapper_bipartite.py
```

### Usage

To start the gRPC server locally

```
python3.6 snet_grpc_wrapper_bipartite.py
```



