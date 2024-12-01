class MathClass:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def factorial(self):
        if self.num1 < 0:
            return "Factorial is not defined for negative numbers."  
        result = 1
        for i in range(1, self.num1 + 1):
            result *= i
        return result

    def isPrime(self):
        if self.num1 < 2:
            return False  
        for i in range(2, int(self.num1 ** 0.5) + 1):  
            if self.num1 % i == 0:
                return False
        return True

    def divisors(self):
        mn = min(self.num1, self.num2)
        common_divisors = []
        for i in range(1, mn + 1):
            if self.num1 % i == 0 and self.num2 % i == 0:
                common_divisors.append(i)
        return common_divisors

def get_number_input(prompt):
    while True:
        try:
            return int(input(prompt))  
        except ValueError:  
            print("Please enter a valid number.")

num1 = get_number_input("Enter the first number: ")
num2 = get_number_input("Enter the second number: ")

c = MathClass(num1, num2)

print("Factorial:", c.factorial())  
print("Common Divisors:", c.divisors())  
print("Is the first number prime?", c.isPrime())  