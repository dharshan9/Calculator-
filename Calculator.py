class Calculator:
    def __init__(self, value=0):
        self.value = value

    def add(self, number):
        """Add a number to the current value."""
        self.value += number
        return self.value

    def subtract(self, number):
        """Subtract a number from the current value."""
        self.value -= number
        return self.value

    def multiply(self, number):
        """Multiply the current value by a number."""
        self.value *= number
        return self.value

    def divide(self, number):
        """Divide the current value by a number."""
        if number == 0:
            raise ValueError("Cannot divide by zero.")
        self.value /= number
        return self.value

    def power(self, number):
        """Raise the current value to the power of a number."""
        self.value **= number
        return self.value

    def sqrt(self):
        """Take the square root of the current value."""
        if self.value < 0:
            raise ValueError("Cannot take the square root of a negative number.")
        self.value **= 0.5
        return self.value

    def get_value(self):
        """Return the current value."""
        return self.value

    def reset(self):
        """Reset the value to zero."""
        self.value = 0
        return self.value

def main():
    # Create an instance of Calculator
    calc = Calculator()
    
    # Perform some operations
    print("Initial Value:", calc.get_value())
    print("Add 10:", calc.add(10))
    print("Subtract 4:", calc.subtract(4))
    print("Multiply by 3:", calc.multiply(3))
    print("Divide by 2:", calc.divide(2))
    print("Power of 3:", calc.power(3))
    print("Square Root:", calc.sqrt())
    print("Reset:", calc.reset())
    print("Current Value:", calc.get_value())

if __name__ == "__main__":
    main()