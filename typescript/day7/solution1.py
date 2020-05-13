import input
newInput=input.input.split("\n")
import re
index=0
commandoMap=dict()

def lijnNaarCommando(instruction):
    lowerCaseCharacters=re.findall(r"[a-z\d]+",instruction)
    operator=re.findall(r"[A-Z]+",instruction)
    if len(operator): 
        operator = operator[0]
    else: 
        operator = None
    lastIndex = len(lowerCaseCharacters) - 1
    commando = {
        'output': lowerCaseCharacters[lastIndex],
        'operator': operator,
        'input': lowerCaseCharacters[0:lastIndex]
    }
    return commando

def zetCommandoInMap(commando):
    commandoMap[str(commando['output'])]= commando

while index<len(newInput):
    commando = lijnNaarCommando(newInput[index])
    zetCommandoInMap(commando)
    index=index+1
print(commandoMap)


# vind a
# reken a uit door delen van a uit te rekenen