"""
Python Program for Compound Interest
"""

def compoundInterest(p,t,r):
    amount = p * (1 + (r / 100)) ** t 
    return amount - p 
    

p = int(input("Enter the Principal: "))
t = int(input("Enter the Time period: "))
r = float(input("Enter the rate (without %): "))

print("Compound interest =", compoundInterest(p,t,r))

