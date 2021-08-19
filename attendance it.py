# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 10:24:29 2020

@author: adeeb
"""

import re

for line in iter(input,''):   #To read all lines in the input till empty string ('') is encountered.
    elemlist=[elem for elem in line if elem.isnumeric() or elem.isspace()]
                              #To extract only numbers from all lines of the input.
                              
result = "".join(elemlist)    #To join all individual digits collected in last step. 
allnums=[result[match.end():(match.end()+3)] for match in re.finditer("160419737", result)]
                              #To search for the pattern and extract the 3 digit Roll No after it.
                              
pres = list(set([int(n) for n in allnums]))  #To convert the list of strings to list of integers.
                                             # "list(set(x))" can be used to remove dublicates.
                                             
absn=set(pres)^set([*range(1,61)])           #To get nos (1-60) that are not present
pres.sort()                                  #Sorting for convenience.

print("Absentees-", absn, "\n\nPresent-", pres, "\n\nTotal present-", len(pres) )
Adeeb_is_awesome=input("Adeeb created me and I serve him with all my heart :) ")