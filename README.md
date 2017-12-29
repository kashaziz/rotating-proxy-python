# Rotating Proxy Servers in Python

Python class making it easy to Rotate through ProxyMesh Proxy Severs.

## Prerequisites

An account with ProxyMesh, either free trial or paid. Set the user name and password in rotatingproxy.py

```
self.user = ""
self.password = "" 
```

## Usage

### Setting the Proxy Server

```
from rotatingproxy import RotatingProxy

rproxy = RotatingProxy()
```

The proxy server can either be set randomly or selected from an available list of proxy servers. 
The active proxy server is saved in a text file which can be accessed as required.

```
rproxy.set_proxy(israndom="r")  # select a random proxy server

rproxy.set_proxy(proxy_num=1)   # select proxy server with index=1 from the list of proxy servers.
```

### Accessing the Proxy Server

```
def get_proxy_from_file():
    # fetches proxy from proxy.txt
    with open("proxy.txt", "r") as f:
        return loads(f.read())
        
proxy = get_proxy_from_file()        
```

The proxy can now be used with requests:

```
import requests
response = requests.get("url-to-fetch", proxies=proxy)
```

### Running the tests
Unit tests are included to check if the proxy is random or selected from the list of proxy.

