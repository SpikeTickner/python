from itertools import count

i = input("i: ") 
x = 1

i = int(i) 

while x <= i:
    prime = True
    for n in range(2, x):
        #print (" n="+str(n)+" x="+str(x))
        if n == 0:
            break
        if x != n and x % n == 0:
            prime = False

    if prime:
        print(x)
    x += 1
