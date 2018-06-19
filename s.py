#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def search(keyword, filename):
    print('generator started')
    f = open(filename, 'r')
    # Looping through the file line by line
    count=1
    for line in f:
        #print('inside for loop----------')
        if keyword in line:
            # If keyword found, return it
            yield line
            count+=1
    f.close()


#for x in search("is","a.txt"): print(x)
