#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import json


no = int(input("how many number http trigger?"))
for i in range(1,no+1):
        #req = request.Request('http://localhost:8080/greeting?name=User')
        end_point='http://localhost:8080/people'
        body={ "firstName" : " ".join(("I am a king ",str(i))) , "lastName" : "dd" }
        #end_point+=str(i)
        req = request.Request(end_point)
        req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(body)
        jsondataasbytes = jsondata.encode('utf-8')   # needs to be bytes
        req.add_header('Content-Length', len(jsondataasbytes))
        print (jsondataasbytes)
        with request.urlopen(req,jsondataasbytes) as f:
            pass#print('Status:', f.status, f.reason)
            for k, v in f.getheaders():
                pass
                #print('%s: %s' % (k, v))
            print('Data:', f.read().decode('utf-8'))
            #print('Data:', json.loads(f.read()) )
