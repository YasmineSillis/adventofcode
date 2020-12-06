import input
newInput=input.input
print(len(newInput))

positiex=0
positiey=0
i=0
newposities=list()
while i<len(newInput):
    if newInput[i]==">":
        positiex = positiex + 1
    if newInput[i]=="<":
        positiex = positiex - 1
    if newInput[i]=="^":
        positiey = positiey + 1
    if newInput[i]=='v':
        positiey = positiey - 1
    positie= str(positiex) + "," + str(positiey)
    if positie not in newposities:
        newposities.append(positie)
    i = i + 1

print(len(newposities))

xSanta=0
ySanta=0
xRobot=0
yRobot=0
iSanta=0
iRobot=1
bezochtehuizen=list()
while iRobot<len(newInput):
    if newInput[iSanta]==">":
        xSanta = xSanta + 1
    if newInput[iSanta]=="<":
        xSanta = xSanta - 1
    if newInput[iSanta]=="^":
        ySanta = ySanta + 1
    if newInput[iSanta]=='v':
        ySanta = ySanta - 1
    if newInput[iRobot]==">":
        xRobot = xRobot + 1
    if newInput[iRobot]=="<":
        xRobot = xRobot - 1
    if newInput[iRobot]=="^":
        yRobot = yRobot + 1
    if newInput[iRobot]=='v':
        yRobot = yRobot - 1
    positieSanta=str(xSanta) + "," + str(ySanta)
    positieRobot=str(xRobot)+","+str(yRobot)
    if positieSanta not in bezochtehuizen:
        bezochtehuizen.append(positieSanta)
    if positieRobot not in bezochtehuizen:
        bezochtehuizen.append(positieRobot)
    iSanta = iSanta + 2
    iRobot = iRobot + 2

print(len(bezochtehuizen))
    