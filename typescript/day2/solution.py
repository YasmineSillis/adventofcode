import input

newInput = input.input.split("\n")
print(len(newInput))

i=0

lijstpakjes=list()
while i<len(newInput):
    stringpakje=newInput[i].split("x")
    index=0
    intpakje=list()
    while index<len(stringpakje):
        intpakje.append(int(stringpakje[index]))
        index = index + 1
    lijstpakjes.append(intpakje)
    pakje = lijstpakjes[i]
    pakje.sort()
    i = i + 1

l=0
w=1
h=2
i=0
papier=0

while i<len(lijstpakjes):
    pakje= lijstpakjes[i] 
    papierpakje = 2*pakje[l]*pakje[w]+2*pakje[w]*pakje[h]+2*pakje[h]*pakje[l]+pakje[l]*pakje[w]
    papier = papier + papierpakje
    i = i + 1

print(papier)

i=0
ribbon=0

while i<len(lijstpakjes):
    pakje=lijstpakjes[i]
    ribbonpakje= 2*pakje[l]+2*pakje[w]+pakje[l]*pakje[w]*pakje[h]
    ribbon = ribbon + ribbonpakje
    i = i + 1

print(ribbon)