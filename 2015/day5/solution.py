import input
newInput= input.input.split("\n")
print(len(newInput))
index=0
nice=list()
while index<len(newInput):
    woord=newInput[index]
    a=woord.count('a')
    e=woord.count('e')
    i=woord.count('i')
    o=woord.count('o')
    u=woord.count('u')
    ab=woord.count('ab')
    cd=woord.count('cd')
    pq=woord.count('pq')
    xy=woord.count('xy')
    aa=woord.count('aa')
    bb=woord.count('bb')
    cc=woord.count('cc')
    dd=woord.count('dd')
    ee=woord.count('ee')
    ff=woord.count('ff')
    gg=woord.count('gg')
    hh=woord.count('hh')
    ii=woord.count('ii')
    jj=woord.count('jj')
    kk=woord.count('kk')
    ll=woord.count('ll')
    mm=woord.count('mm')
    nn=woord.count('nn')
    oo=woord.count('oo')
    pp=woord.count('pp')
    qq=woord.count('qq')
    rr=woord.count('rr')
    ss=woord.count('ss')
    tt=woord.count('tt')
    uu=woord.count('uu')
    vv=woord.count('vv')
    ww=woord.count('ww')
    xx=woord.count('xx')
    yy=woord.count('yy')
    zz=woord.count('zz')
    if a+e+i+o+u>=3 and ab+cd+pq+xy==0 and aa+bb+cc+dd+ee+ff+gg+hh+ii+jj+kk+ll+mm+nn+oo+pp+qq+rr+ss+tt+uu+vv+ww+xx+yy+zz>0:
        nice.append(woord)
    index = index + 1

print(len(nice))