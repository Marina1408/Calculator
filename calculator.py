# Define a class called Calculator to perform basic arithmetic operations
class Calculator:
    def __init__(self, num1, num2, operation):
        self.num1 = num1
        self.num2 = num2
        self.operation = operation

    # Define a method for addition that takes two arguments and returns their sum
    def _add (self):
        return self.num1 + self.num2

    # Define a method for subtraction that takes two arguments and returns their difference
    def _subtract (self):
        return self.num1 - self.num2

    # Define a method for multiplication that takes two arguments and returns their product
    def _multiply (self):
        return self.num1 * self.num2

    # Define a method for division that takes two arguments and returns the result if the denominator is not zero,
    # or an error message if the denominator is zero
    def _divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return ("Cannot divide by zero.")

    def operate(self):
        if self.operation == "add":
            return self._add()
        if self.operation == "subtract":
            return self._subtract()
        if self.operation == "multiply":
            return self._multiply()
        if self.operation == "divide":
            return self._divide()



