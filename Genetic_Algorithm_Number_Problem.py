from random import randint,random

def individual(length,imin,imax):
    return [randint(imin, imax) for i in range(length)]

def population(count,length,imin,imax):
    return [individual(length, imin, imax)   for i in range(count)]
def fitness(individual,target):
    total=sum(individual)
    return abs(total-target)
def graded(population,target):
    pf1=[fitness(i, target) for i in population]
    af=sum(pf1)/(len(population)*1.0)
    return af
def evolve(p,target,r=0.2,c=0.05,m=0.01):
    fil=[(fitness(i, target),i) for i in p ]
    spi=[i for (f,i) in sorted(fil)]
    r1=int(len(p)*r)
    #spi=[t[1] for t in sp]
    parents=spi[:r1]
    for i in spi[r1:]:
        if c>random():
            parents.append(i)
pn=[]
    while len(pn) <len(p):

        i1=randint(0,len(parents)-1)
        i2=randint(0,len(parents)-1)
        if i1==i2:
            continue


        p1=parents[i1]
        p2=parents[i2]


        p3=p1[0:5]+p2[5:10]
        p4=p2[0:5]+p1[5:10]
pn.append(p3)
pn.append(p4)

for i in pn:
        if random()<m:
            dtm=randint(0,len(i)-1)
            i[dtm]=randint(min(i), max(i))    

return pn



a=population(40,10,1,100)
i=0
while i<10:
    z=evolve(a,371)
    a=z
    print(graded(a,371))
i+=1


print(a)    
