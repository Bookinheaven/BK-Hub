class MathOperations:
    @classmethod
    def add(cls, x, y):
        return x+ y
    
    @staticmethod
    def multiply(x, y):
        return x * y
    
sum_result = MathOperations.add(3, 5)
print(f"Sum: {sum_result}")

product_result = MathOperations.multiply(2, 4)
print(f"Product: {product_result}")