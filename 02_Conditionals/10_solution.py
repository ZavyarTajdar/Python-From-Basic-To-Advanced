pet = str(input("Enter your pet specie : ")).lower()
age = int(input("Enter your pet age : "))

if pet == "dog" :
    if age < 2 :
        print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Puppy Food")
    elif 2 <= age <= 7 :
        print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Adult Dog Food")
elif pet == "cat" :
    if age < 5 :
        print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Kitten Food")
    elif 5 <= age <= 10 :
        print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Adult Cat Food")
    else :
        print(f"Your Pet {pet}\'s age is {age}, then you should feed him/her with Senior Cat Food")  
else : 
    print("Invalid Choice")  