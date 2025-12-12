pet = str(input("Enter your pet specie : ")).lower()
age = int(input("Enter your pet age : "))

if pet == "dog" and age > 2 :
    print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Puppy Food")
elif pet == "cat" and age > 5 :
    print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Senior Cat Food")  
else : 
    print("Invalid Choice")  