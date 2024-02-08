"""
Write a program to ask username and password as input and check whether is "karunya" or not. 
If it is valid display the message as "Login Successful" otherwise "Login Failed".
"""
print("\t\tLogin Page")
username = str(input("Username: "))
password = str(input("Password: "))

if (username == "karunya" and password == "karunya"):
    print("Login Successful!")
else: 
    print("Login Failed!")

