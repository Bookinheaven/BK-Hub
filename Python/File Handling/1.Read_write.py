with open("./file_w.txt", "w+") as file:
    file.write('First Line\nSecond Line\nThird Line')
# with open("./file_w.txt", "r+") as file:
    file.seek(0)
    data = file.read()
    print(data)
