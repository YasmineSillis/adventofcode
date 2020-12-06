import input;

newInput = input.input.split("\n")
print(newInput)

def function1 (xString):
    lijst = list(map(int, xString.split("x")));()
    lijst.sort()
    return lijst;

pakjes = list(map(function1, newInput))
print(pakjes)

l = 0
w = 1
h = 2

totaalPapier = 0
index = 0
while(index < len(pakjes)):
    gesorteerdPakje = pakjes[index]
    papier = 2*gesorteerdPakje[l]*gesorteerdPakje[w] + 2*gesorteerdPakje[w]*gesorteerdPakje[h] + 2*gesorteerdPakje[h]*gesorteerdPakje[l] + gesorteerdPakje[l]*gesorteerdPakje[w]
    totaalPapier = totaalPapier + papier
    index = index + 1

print("totaalPapier", totaalPapier);

index = 0
totaalRibbon = 0
while (index < len(pakjes)):
    gesorteerdPakje = pakjes[index]
    ribbon = 2*gesorteerdPakje[l] + 2*gesorteerdPakje[w] + gesorteerdPakje[l]*gesorteerdPakje[w]*gesorteerdPakje[h]
    totaalRibbon = totaalRibbon + ribbon
    index = index + 1

print("totaalRibbon", totaalRibbon)
