import os
import json
import urllib2

while True:
    ip=raw_input("what is your traget ip address:")
    url = "http://ip-api.com/json/"
    response = urllib2.urlopen(url+ip)
    data = response.read()
    values = json.loads(data)
    print("ip: "+ values['query'])
    print("city: "+ values['city'])
    print("ISP: "+ values['isp'])
    print("Country: "+ values['country'])
    print("Region: "+ values['region'])
    print("Time Zone: "+ values['timezone'])

    break 
