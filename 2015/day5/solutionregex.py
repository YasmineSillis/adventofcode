import input
newInput= input.input.split("\n")
print(len(newInput))
import re
index=0
nice=list()
while index<len(newInput):
    woord=newInput[index]
    vowels=re.findall("[aeiou]", woord)
    group=re.findall("ab", woord)+re.findall("cd",woord)+re.findall("pq",woord)+re.findall("xy",woord)
    double=re.findall(r"([a-z])\1",woord)
    if len(vowels)>=3 and len(group)==0 and len(double)>0:
        nice.append(woord)
    index=index+1
print(len(nice))