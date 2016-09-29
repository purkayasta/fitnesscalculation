"""
Sunny,Pritom Purkayasta
Genetics Algorithm
ID:13-24183-2

"""

import random
print ("New Parents are")
a=[6,5,4,1,3,5,3,2]
b=[8,7,1,2,6,6,0,1]
c=[2,3,9,2,1,2,8,5]
d=[4,1,8,5,2,0,1,4]
print (a)
print (b)
print (c)
print (d)

totalofa = (a[0]+a[1])-(a[2]+a[3])+(a[4]+a[5])-(a[6]+a[7])
totalofb = (b[0]+b[1])-(b[2]+b[3])+(b[4]+b[5])-(b[6]+b[7])
totalofc = (c[0]+c[1])-(c[2]+c[3])+(c[4]+c[5])-(c[6]+c[7])
totalofd = (d[0]+d[1])-(d[2]+d[3])+(d[4]+d[5])-(d[6]+d[7])

print ("Total of A = ",totalofa)
print ("Total of B = ",totalofb)
print ("Total of C = ",totalofc)
print ("Total of D = ",totalofd)

Alltotal = totalofa+totalofb+totalofc+totalofd
print ("All Total Is = ",Alltotal)

avg = (Alltotal/4)
print ("Average is = ",avg)

maxlist = [totalofa,totalofb,totalofc,totalofd]
print ("First Max Value ",max(maxlist))


maxlist.remove(max(maxlist))
print ("Second Max Value ",max(maxlist))

print ("Cross Over the values of a and b")
print ("------")
print ("-------------")
print ("--------------------")

"""
def swap(number1,number2):
    temp = number1
    number1 = number2
    number2 = temp
    del temp

"""
c = list(a)
d = list(b)
def swaping():   
    temp = d[4],d[5],d[6],d[7]
    d[4],d[5],d[6],d[7] = c[4],c[5],c[6],c[7]
    c[4],c[5],c[6],c[7] = temp
    del temp

swaping()
print ("Before Swaping")
print (a)
print (b)
print ("After Swaping")
print (c)
print (d)
print ("Mutated new values")
print ("------------")
print ("---------------------")
print ("--------------------------------")
def mutation():
    d[4] = random.randint(1,9)
    c[4] = random.randint(1,9)

mutation()
print ("New Parents")
print (a)
print (b)
print (c)
print (d)

totalofa = (a[0]+a[1])-(a[2]+a[3])+(a[4]+a[5])-(a[6]+a[7])
totalofb = (b[0]+b[1])-(b[2]+b[3])+(b[4]+b[5])-(b[6]+b[7])
totalofc = (c[0]+c[1])-(c[2]+c[3])+(c[4]+c[5])-(c[6]+c[7])
totalofd = (d[0]+d[1])-(d[2]+d[3])+(d[4]+d[5])-(d[6]+d[7])

print ("Total of A = ",totalofa)
print ("Total of B = ",totalofb)
print ("Total of C = ",totalofc)
print ("Total of D = ",totalofd)

Alltotal = totalofa+totalofb+totalofc+totalofd
print ("All Total Is = ",Alltotal)

avg = (Alltotal/4)
print ("Average is = ",avg)

maxlist = [totalofa,totalofb,totalofc,totalofd]
print ("First Max Value ",max(maxlist))


maxlist.remove(max(maxlist))
print ("Second Max Value ",max(maxlist))
