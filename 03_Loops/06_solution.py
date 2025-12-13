factorial_num = int(input("Enter a number to calculate its factorial: "))

factorial = 1

while factorial_num > 0:
    factorial *= factorial_num
    factorial_num -= 1
print("The factorial is:", factorial)