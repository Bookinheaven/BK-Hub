print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")
class Main:
    def __init__(self):
        self.expression = ""
        self.operators = ['+', "-", "/","*", "^"]
        self.stack = []
        self.output = []

    def input_expression(self):
        self.expression = (input("Enter the Expression: ")).replace(" ", "")
        self.stack = []
        self.output = []

    def InfixToPostfix(self):
        def precedence(element: str):
            if element == '^':
                return 3
            elif element == '*' or element == '/':
                return 2
            elif element == '+' or element == '-':
                return 1
            else:
                return 0
        for index in range(len(self.expression)):
            char = self.expression[index]
            if char.isalnum():
                self.output.append(char)
            elif char == "(":
                self.stack.append(char)
            elif char in self.operators:
                if self.stack and self.stack[-1] != '(':
                    if precedence(self.stack[-1]) > precedence(char):
                        self.output.append(self.stack[-1])
                        self.stack[-1] = char
                    elif precedence(self.stack[-1]) < precedence(char):
                        self.stack.append(char)
                    elif precedence(self.stack[-1]) == precedence(char):
                        self.output.append(self.stack[-1])
                        self.stack[-1] = char
                else:
                    self.stack.append(char)
            elif char == ')':
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()
        while self.stack:
            self.output.append(self.stack[-1])    
            self.stack.pop()
        print("Postfix Expression: ",*self.output, sep='')
    def EvaluatePostfix(self):
        for char in self.expression:
            if char.isdigit():
                self.stack.append(int(char))
            elif char in self.operators:
                if len(self.stack) < 2:
                    print("Error: Invalid expression")
                    return
                op1 = self.stack.pop()
                op2 = self.stack.pop()
                if char == '+':
                    self.stack.append(op2 + op1)
                elif char == '-':
                    self.stack.append(op2 - op1)
                elif char == '*':
                    self.stack.append(op2 * op1)
                elif char == '/':
                    self.stack.append(op2 / op1)
                elif char == '^':
                    self.stack.append(op2 ** op1)
        print("Postfix Expression Evaluation:", self.stack[0])
instance = Main()
while True:
    print("\nMenu:")
    print("1. Infix to Postfix")
    print("2. Evaluate Postfix Expression")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        instance.input_expression()
        instance.InfixToPostfix()

    elif choice == 2:
        instance.input_expression()
        instance.EvaluatePostfix()

    elif choice == 3:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")

#231*+9-
#100 200 + 2 / 5 * 7 +
#A+ (B*C-(D/E^F)*G)*H == ABC*DEF^/G*-H*+
#A+B-(C*D-E)+F == AB+CD*E--F+

