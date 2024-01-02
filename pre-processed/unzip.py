# importing the zipfile module 
from zipfile import ZipFile 
from os import system

# loading the temp.zip and creating a zip object 
with ZipFile("NOFLY.csv.zip", 'r') as zObject: 
    zObject.extractall( path="NOFLY.csv")
    system('rm -f NOFLY.csv.zip')