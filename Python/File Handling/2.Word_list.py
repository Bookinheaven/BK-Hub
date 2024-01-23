fp = open("./file_w.txt", 'r')
# global words
words = []
for line in fp:
    words.extend(line.split())
print(words)
