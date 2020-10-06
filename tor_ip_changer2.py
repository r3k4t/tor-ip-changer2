import os
import sys
import json
import time
import requests
import urllib.request

def get_current_ip():
    session = requests.session()

    
    session.proxies = {}
    session.proxies['http']='socks5://localhost:9050'
    session.proxies['https']='socks5://localhost:9050'

    try:
        r = session.get('http://ifconfig.me/ip')
    except Exception as e:
        print  (e)
    else:
        return r.text


if __name__ == "__main__":
    for i in range(1):
        os.system("clear")
        print("            ### TOR-IP-CHANGER2 ###         ")
        time.sleep(1)
        print("     #### Author : Rahat Khan Tusar(RKT) ####")
        time.sleep(2)
        print(" ###### Github : https://github.com/r3k4t ######")
        print
        time.sleep(2)
        print ("Old Idenity")
        time.sleep(2)
        print (get_current_ip())
        time.sleep(2)
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url + get_current_ip() )
        data = response.read()
        rkt = json.loads(data)
        print (data)
        os.system("sudo service tor restart")
        time.sleep(2)
        print ("New Idenity")
        time.sleep(2)
        print (get_current_ip())
        time.sleep(2)
        url = "http://ip-api.com/json/"
        response = urllib.request.urlopen(url + get_current_ip() )
        data = response.read()
        rkt = json.loads(data)
        print (data)
        print ("check tor connection")
        print ("Link:http://check.torproject.org")
     

        
