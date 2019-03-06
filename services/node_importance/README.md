# Network Analytics Services
## Node Importance


### Welcome
This repository contains various network analytics services for SingularityNET. The services are wrapped using gRPC. To work with the service wrapper code "snet_grpc_wrapper.py" and other code that make use of gRPC functionality, run the following in the "services" directory

### Install prerequisites
#### Using pip
```
pip install -r requirements.txt
```


### Setup
- run the following command to generate gRPC classes for Python in node_importance folder
```bash
$ python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. service_spec/node_importance.proto
```


## Usage
To run the server
```bash
# on project directory this will start the server 
$ python  start_service.py
```



## Authors
- [Israel Abebe](https://github.com/IsraelAbebe) - [SingularityNet.io](https://singularitynet.io/)
