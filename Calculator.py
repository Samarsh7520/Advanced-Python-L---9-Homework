print("Welcome to the Calculator App")
print("You can choose any of the operations")
print("\n1. Addition")
print("\n2. Subtraction")
print("\n3. Multiplication")
print("\n4. Division\n")

operation = input("Please enter your choice: ")
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

if operation == "1":
    result = number1 + number2
    print("The result after addition is",result)
    
elif operation == "2":
    result = number1 - number2
    print("The result after subtraction is", result)

elif operation == "3":
    result = number1 * number2
    print("The result after multiplication is",result)

elif operation == "4":
    result = number1 / number2
    print("The result after division is",result)

else:
    print("Incorrect Option, Please choose a number between 1 and 4")