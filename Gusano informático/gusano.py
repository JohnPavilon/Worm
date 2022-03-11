"""
Created on Wed Mar  9 20:43:33 2022

@author: jonqt
"""

from sys import argv
import os

script = argv
name = str(script[0])
print (name) 

for i in range(0,2):
 directorio = "copia"+str(i)
 os.system("mkdir "+directorio)
 os.system("copy gusano.py"+" "+directorio)
 
fd = os.open(name, os.O_RDONLY)
readBytes = os.read(fd, 500)
  
print(readBytes)

os.close(fd)