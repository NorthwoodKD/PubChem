# PubChem

This project is to identify hazardous products (for shipping and storage classification)

python snip that uses the pubchem wrapper to do the following:
1) takes SMILES string to find the CID
2) using CID, check for LCSS
3) pull back GHS information from LCSS

The following modules are utilized:
pubchempy
urllib.requests
bs4

It NEEDS to be refractored and commented
