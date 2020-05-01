import input
newInput= input.input.split("\n")
print(len(newInput))
import re
index=0
nice=list()
while index<len(newInput):
    woord=newInput[index]
    print(woord)
    double=re.findall(r"([a-z][a-z]).*\1",woord)
    triple=re.findall(r"([a-z]).\1",woord)
    if len(double)>0 and len(triple)>0:
        nice.append(woord)
    index=index+1
print(len(nice))