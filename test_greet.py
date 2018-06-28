#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request


for i in range(1,10):
	#req = request.Request('http://localhost:8080/greeting?name=User')
	end_point='http://localhost:8080/greeting?name=User'
	end_point+=str(i)
	req = request.Request(end_point)
	req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
	with request.urlopen(req) as f:
	    print('Status:', f.status, f.reason)
	    for k, v in f.getheaders():
	        print('%s: %s' % (k, v))
	    print('Data:', f.read().decode('utf-8'))
