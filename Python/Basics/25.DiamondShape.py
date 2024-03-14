n = 5
for i in range(1,n+1):
    print(" "*(n+1-i),end="")
    print("* "*i)
for i in range(n-1,0,-1):
    print(" "*(n+1-i),end="")
    print("* "*i)

n= 5
for x in range(n):
    for y in range(x,n+1):
        print(" ",end="")
    for z in range(x):
        print("*", end=" ")
    print()
for z in range(n):
    print(' *', end="")
print()
for x in range(n):
    for z in range(x+2):
        print(" ", end="")
    for y in range(x,n-1):
        print("*",end=" ")
    print()