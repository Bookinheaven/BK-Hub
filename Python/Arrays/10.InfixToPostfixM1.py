class Infix:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")
        self.stack = []
        self.output = []
    def checkPrecedence(self, item):
            if item == "^":
                return 3
            elif item == "*" or item == "/":
                return 2
            elif item == "+" or item == "-" :
                return 1
            else:
                return 0
    def convertToPostfix(self):
        for char in self.expression:
            if char.isalpha():
                self.output.append(char)
            elif char == '(':
                self.stack.append(char)
            elif char == ')':
                print(self.stack)
                while self.stack and self.stack[-1] != '(':
                    self.output.append(self.stack.pop())
                self.stack.pop()  # Remove '(' from the stack
            else:
                while (self.stack and self.stack[-1] != '(' and 
                        self.checkPrecedence(char) <= self.checkPrecedence(self.stack[-1])):
                    self.output.append(self.stack.pop())
                self.stack.append(char)
        
        while self.stack:
            self.output.append(self.stack.pop())
    
        return ''.join(self.output)
 
               
# ABC*DEF^/G*-H*+
exp = Infix("A+ (B*C-(D/E^F)*G)*H")
postfix = exp.convertToPostfix()
print(postfix)