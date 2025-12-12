print("Enter your Fruit Color \n 1 : Green \n 2 : Yellow \n 3 : Brown ")

banana_Color = str(input("Enter the color of the fruit: "))

if banana_Color == "Green" or banana_Color == "green" :
    print(f"Banana Color Is {banana_Color}, Which mean it is Unripe")
elif banana_Color == "Yellow" or banana_Color == "yellow" :
    print(f"Banana Color Is {banana_Color}, Which mean it is Ripe")
elif banana_Color == "Brown" or banana_Color == "brown" :
    print(f"Banana Color Is {banana_Color}, Which mean it is Overripe")
else : 
    print("Invalid Input")