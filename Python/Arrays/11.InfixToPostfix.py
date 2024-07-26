

class Main:
    def __init__(self):
        self.expression = (input("Enter the expressions: ")).replace(" ","")
        self.stack = []
        self.operators = ['+', "-", "/","*", "^"]
        self.output = []
    def InfixToPostfix(self):
        def is_empty():
            return len(self.stack) == 0
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
        print(*self.output, sep='')
instance = Main()#A+ (B*C-(D/E^F)*G)*H 
#"A+B-(C*D-E)+F"
instance.InfixToPostfix()
# ABC*DEF^/G*-H*+
