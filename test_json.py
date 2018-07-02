#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib.request
import urllib.parse


#url = 'https://api.spotify.com/v1/search?type=artist&q=snoop'
url='http://gturnquist-quoters.cfapps.io/api/random'
f = urllib.request.urlopen(url)
print(f.read().decode('utf-8'))
