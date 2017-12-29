# rotating proxy generated from proxy-mesh api 
from random import randrange
import requests
import json


class RotatingProxy():
    '''        
    sets, deletes, fetches proxy from proxymesh service
    '''

    def __init__(self):
        self.base_url = "https://proxymesh.com"
        self.user = "<username>"
        self.password = "<password>"
        self.proxy_list = ["us-dc.proxymesh.com:31280", "us-ca.proxymesh.com:31280", "us-ny.proxymesh.com:31280"
                        , "us-wa.proxymesh.com:31280", "us-il.proxymesh.com:31280", "us.proxymesh.com:31280"
                        , "us-fl.proxymesh.com:31280", "uk.proxymesh.com:31280", "au.proxymesh.com:31280"
                        , "fr.proxymesh.com:31280", "jp.proxymesh.com:31280", "ch.proxymesh.com:31280"
                        , "de.proxymesh.com:31280", "nl.proxymesh.com:31280", "sg.proxymesh.com:31280"]        

    def fetch_proxy(self):
        response = requests.get(self.base_url+"/api/proxies/", auth=(self.user, self.password))
        if response.status_code == 200:
            proxy = response.json()
            if len(proxy['proxies']) > 1:
                fp = [p for p in proxy['proxies'] if 'open' not in p][0] 
            else:
                fp = proxy['proxies'][0]
            return fp

    def write_proxy(self, fp):
        '''
        prepare proxy with http and auth, also save it proxy.txt
        '''
        fproxy = {"http": "http://"+self.user+":"+self.password+"@"+fp, "https": "http://"+self.user+":"+self.password+"@"+fp}    
        with open("proxy.txt", "w") as f:
            f.write(json.dumps(fproxy))

    def delete_proxy(self, proxy_host):
        response = requests.post(self.base_url+"/api/proxy/delete/", data={'proxy': proxy_host}, auth=(self.user, self.password))

    def set_proxy(self, israndom="r", proxy_num=None):
        '''
        Sets a proxy in ProxyMesh dashboard via API call
        - fetch current proxy
        - delete current proxy
        - set new proxy from the list of proxies either based on index or pick a random proxy
        '''

        print("before setting {}".format(self.fetch_proxy()))
        # delete current proxy
        self.delete_proxy(self.fetch_proxy())

        # get a proxy from proxy list
        if israndom is not None:
            # set a random proxy
            rproxy = self.proxy_list[randrange(0, len(self.proxy_list)-1)]
        else:    
            if proxy_num is not None and proxy_num <= len(self.proxy_list):
                rproxy = self.proxy_list[proxy_num]
            else:
                # set first proxy in the list
                rproxy = self.proxy_list[0]

        # set this proxy as default proxy
        try:
            response = requests.post(self.base_url+"/api/proxy/add/", data={'proxy': rproxy}, auth=(self.user, self.password))
            self.write_proxy(self.fetch_proxy())

            print("after setting {}".format(self.fetch_proxy()))      
        except Exception as e:
            print(e)

        return
