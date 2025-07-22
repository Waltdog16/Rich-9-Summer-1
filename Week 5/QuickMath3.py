class Calculator:
    def add(self, a, b):
        return a + b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b
    
    def subtract(self, a, b):
        return a - b

calculator = Calculator()


sum = calculator.add(25,78)
difference = calculator.subtract(10, 5)
product = calculator. multiply(5, 8)
dividend = calculator. divide(32, 8)
print(sum)
print(difference)
print(product)
print(dividend)

