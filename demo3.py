# Calculator in Python

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def multi(x, y):
    return x * y

def div(x, y):
    return x / y

def remend(x, y):
    return x % y

print("Please select an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Remainder")

choice = input("Enter your choice (1/2/3/4/5):")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if choice == '1':
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print(f"{num1} - {num2} = {sub(num1, num2)}")
elif choice == '3':
    print(f"{num1} * {num2} = {multi(num1, num2)}")
elif choice == '4':
    print(f"{num1} / {num2} = {div(num1, num2)}")
elif choice == '5':
    print(f"{num1} % {num2} = {remend(num1, num2)}")
else:
    print("Invalid choice. Please select a valid operation.")
