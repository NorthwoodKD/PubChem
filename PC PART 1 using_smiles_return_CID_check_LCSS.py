#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 15:49:48 2017

@author: zac
"""

import pubchempy as pcp
import urllib.request
import bs4 as BS


products = {}

with open('LabNetworkSearch.txt') as l:
    for line in l:
        information = line.split()
        productID = information[0]
        smile = information[1]
        products[productID] = {"SMILES": smile} 
        try:
            getCID = str(pcp.get_cids(smile, 'smiles'))
            getCID = getCID.replace("[", "")
            getCID = getCID.replace("]", "")
            products[productID]["CID"] = getCID
        except:
            products[productID]["CID"] = "NA"
            print('Record completed, checking the next record')
        else:
            print('Record completed, checking the next record')    
              
print("CID added to the dictionary\n")

partOne = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/'
partTwo = '/XML?heading=LCSS'        

for product, product_info in products.items():   
    try:
        xml_data = urllib.request.urlopen(partOne + product_info['CID'] + partTwo).read()
        xml = BS.BeautifulSoup(xml_data, 'xml')
        
    except:       
        products[product]["LCSS"] = 'NO'
    else:
        for item in xml.findAll('BoolValue'):
            products[product]["LCSS"] = 'YES'

print("\nLCSS values added to file, now retreiving GHS data\n")

partOneLcss = "https://pubchem.ncbi.nlm.nih.gov/rest/pug_view/data/compound/"
partTwoLcss = "/XML/?"
    
file = open("TEST2.txt", "w")
for product, product_info in products.items():
        if product_info["LCSS"] == "YES":
                file.write(product + " " + product_info["CID"] + " " + product_info["LCSS"] + "\n")
file.close()    

#print("File ready")


#partTwoT = '/XML/?'
#
#for product, product_info in products.items():
#
#    xml_data = urllib.request.urlopen(partOne + product_info['CID'] + partTwoT)
#    xml = BS.BeautifulSoup(xml_data, 'lxml')
#    
#    sections = []
#    for section in xml.find_all('stringvalue'):
#        sections.append(section)
#    
#    if len(sections) > 0:
#        sections_xml = sections[-1].string
#        
#        soupy = BS.BeautifulSoup(sections_xml, 'lxml')
#        
#        try:
#            products[product]['GHS'] = soupy.find('img').get('title')
#            
#        except:
#            products[product]['GHS'] = 'NA'
#
#file = open("LabNetworkSearch_RESULTS.txt", "w")
#for product, product_info in products.items():
#    file.write(product + ":" + product_info["CID"] + ":" + product_info["LCSS"] + ":"+ product_info['GHS'] + "\n")
#file.close()    
#
#print("File ready")


