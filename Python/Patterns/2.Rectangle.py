def printRectangle(l: int, b: int) -> None :
    for _ in range(l):
        for _ in range(b):
            print(" * ", end="")
        print()

printRectangle(5, 7)