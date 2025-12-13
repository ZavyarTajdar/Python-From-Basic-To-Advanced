while True:
    input_value = int(input("Enter a number (or '0' to quit): "))
    if input_value == 0:
        break
    if 1 <= input_value <= 10:
        print("Valid input:", input_value)
    else:
        print("Invalid input, please try again.")