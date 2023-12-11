"""
Python Program for Simple Interest
"""
def simpleInterest(p,t,r):
    return (p * t * r) / 100
    

p = int(input("Enter the Principal: "))
t = int(input("Enter the Time period: "))
r = float(input("Enter the rate (without %): "))

print("Simple interest =", simpleInterest(p,t,r))

