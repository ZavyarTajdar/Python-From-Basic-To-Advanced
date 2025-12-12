distance = int(input("Enter your distance In km : "))

if distance < 3 :
    print(f"Your Distance is {distance}, You Should cover your Distance by Walk ")
elif distance >= 3 and distance <= 15 :
    print(f"Your Distance is {distance}, You Should cover your Distance by Bike")
else :
    print(f"Your Distance is {distance}, You Should cover your Distance by Car")