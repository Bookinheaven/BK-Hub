import pickle
class basic:
    def __init__(self, name):
        self.name = name
        self.basic_are = 12
basic1 = basic(input("Enter your name : "))
with open("/bk.pkl","wb") as file:
    pickle.dump(basic1,file)

print('Done')

with open("/bk.pkl","wb") as file:
    basic2 = pickle.load(file)
    print(f"{basic2.name}")