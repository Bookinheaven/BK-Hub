class less_than:
    def __init__(self,num1):
        self.num1=num1
    def __str__(self):
        return "Bool:{}".format(self.num1)
    def __lt__(self, ob):
        return less_than(self.num1<ob.num1)
d1=less_than(32)

d2=less_than(2)

d3=d1<d2
print(d3)


class powering:
    def __init__(self,num):
        self.num=num
    def __str__(self):
        return "Number:{}".format(self.num)
    def __pow__(self, ob):
        return powering(self.num**ob)
d1=powering(2)
d3=d1**2
print(d3)

class powering:
    def __init__(self,num):
        self.num=num
    def __str__(self):
        return "Number:{}".format(self.num)
    def __pow__(self, ob):
        return powering(self.num**ob.num)
d1=powering(2)
d2=powering(3)
d3=d1**d2
print(d3)

class Distance:
    def __init__(self,feet,inches):
        self.feet=feet
        self.inches=inches
    def __str__(self):
        return "Feet:{},Inches:{}".format(self.feet,self.inches)
    def __sub__(self, ob):
        return Distance(self.feetob.feet,self.inches-ob.inches)
d1=Distance(10,5)
d2=Distance(7,4)
d3=d1-d2
print(d3)