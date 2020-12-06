import input
newInput=input.input.split("\n")
import numpy
matrix=numpy.zeros((1000,1000))
import re
index=0
posities=list()
while index<len(newInput):
    instruction=newInput[index]
    positie=re.findall(r"(\d+)",instruction)
    actie=re.findall(r"(\w+) \d",instruction)
    posities.append(positie)
    positie.append(actie[0])
    index=index+1
print(posities)
index=0
while index<len(posities):
    instruction=posities[index]
    for rij in range(int(instruction[0]),int(instruction[2])+1):
        for kolom in range(int(instruction[1]),int(instruction[3])+1):
            if instruction[4]=="on":
                matrix[rij][kolom]=1
            elif instruction[4]=="off":
                matrix[rij][kolom]=0
            elif instruction[4]=="toggle":
                if matrix[rij][kolom]==0:
                    matrix[rij][kolom]=1
                else:
                    matrix[rij][kolom]=0
            else:
                raise "problem"
    index=index+1
lightson=numpy.count_nonzero(matrix)
print(lightson)

