day = "Wednesday"
age = int(input("Enter your age : "))

if age < 18 :
    print(f"your Ticket price is 8$")
    if day == "Wednesday" :
        print(f"You Got Discount Of 2$ On Wednesday")
elif age >= 18 :
    print(f"Your Ticket price is 12$")
    if day == "Wednesday" :
        print(f"You Got Discount Of 2$ On Wednesday")
