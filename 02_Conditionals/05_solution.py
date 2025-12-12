weather = str(input("Enter Your Weather Condition : ")).lower()

if weather == 'sunny' :
    print(f"Today is {weather} day , You Should Go for a walk")
elif weather == 'rainy' :
    print(f"Today is {weather} day , You Should Read a book")
elif weather == 'snowy' :
    print(f"Today is {weather} day , You Should Build a snowman")
else :
    print("Invalid Input")