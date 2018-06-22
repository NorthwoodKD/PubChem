#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:27:32 2017

@author: zac
"""

import urllib.request
from bs4 import BeautifulSoup

partOne = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/'
partTwo = '/XML/?'

with open('TEST2.txt') as l:
    lines = l.readlines()

results = []

for line in lines:
    productID = line.split(" ")[0]
    cid = line.split(" ")[1]
    xml_data = urllib.request.urlopen(partOne + cid + partTwo)
    xml = BeautifulSoup(xml_data, 'lxml')
    
    sections = []
    for section in xml.find_all('stringvalue'):
        sections.append(section)
    
    if len(sections) > 0:
        sections_xml = sections[-1].string
        
        soupy = BeautifulSoup(sections_xml, 'lxml')
        
        try:
            result = (productID + " : " + cid + " : " + soupy.find('img').get('title'))
            results.append(result)
            print(result)
        except:
            result = (productID + " : " + cid + " : " + "FAIL")
            results.append(result)
            print(result)

file = open("TEST_RESULTS2.txt", "w")
for result in results:
    file.write(result + "\n")
file.close()    

print("File ready")