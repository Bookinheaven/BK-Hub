def printTriangleN(n: int) -> None :
    for i in range(n):
        for _ in range(i + 1):
            print(" * ", end="")
        print()

printTriangleN(5)

print()

def printTriangleR(n: int) -> None :
    for i in range(n, 0, -1):
        for _ in range(i):
            print(" * ", end="")
        print()

printTriangleR(5)


print()

def printPyramidN(n: int) -> None :
    for i in range(n):
        for j in range(n - i): # space
            print("   ", end="")
        for k in range(2*i + 1): # stars
            print(" * ", end="") 
        
        print()

printPyramidN(5)