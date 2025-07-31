def printSquare(n: int) -> None :
    for _ in range(n):
        for _ in range(n):
            print(" * ", end="")
        print()

printSquare(5)