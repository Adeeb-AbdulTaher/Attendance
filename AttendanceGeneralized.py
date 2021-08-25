# -*- coding: utf-8 -*-
"""
Created on Sun Wed 23 21:01:03 2020

@author: adeeb
"""

import re

elemlist=[]
try:
    for line in iter(input,''):
        elemlist+=[elem for elem in line if elem.isnumeric()]
except EOFError:
    pass

result = "".join(elemlist)

check= re.search("1604", result)
x=check.start()

if int(result[(x+9):(x+12)])<61:
    rollnos=[*range(1,61)]
    sec="Section A"
else:
    rollnos=[*range(61,121)]
    sec="Section B"

branches={"737": "IT", "735": "ECE","733":"CSE","736":"MECH"}
print('The Class is',branches.get(result[(x+6):(x+9)])," ", sec)

pattern=result[x:(x+9)]
allnums=[result[match.end():(match.end()+3)] for match in re.finditer(pattern, result)]
    
pres = list(set([int(n) for n in allnums]))
absn=set(pres)^set(rollnos)
pres.sort()

print("\nAbsentees-", absn, "\n\nPresent-", pres, "\n\nTotal present-", len(pres) )
try:
    Adeeb_is_cool=input("Adeeb is my master :)")
except EOFError:
    pass
