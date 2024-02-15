class Pen:
    def __init__(self, name, cost, time):
        self.pen_name = name
        self.pen_cost = cost
        self.pen_time = time
        self.change(self.pen_name)
    def change(self, var):
        var = 'new'
    def set_name(self, name):
        self.pen_name = name
    def set_cost(self, cost):
        self.pen_cost = cost
    def set_time(self, time):
        self.pen_time = time
    def __str__(self):
        return f"Pen name: {self.pen_name}\nPen cost: {self.pen_cost}\nPen Time: {self.pen_time}\n"
    
pen_1 = Pen(name="Parker", time="1920", cost="999")
pen_2 = Pen(name="Cello", time="1900", cost="9")
pen_3 = Pen(name="OX", time='1910', cost='10')

pens = [pen_1,pen_2,pen_3]
for pen in pens:
    print(pen)