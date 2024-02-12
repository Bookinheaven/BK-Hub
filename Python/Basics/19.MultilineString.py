string = []
print("Enter the multiline input:")
y = True
while y == True:
    x = input()
    if x == 'exit':
        y = False
    else:
        string.append(x)
print(string)
