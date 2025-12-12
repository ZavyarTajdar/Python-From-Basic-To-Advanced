age = int(input("Enter Your Age: "))

if age < 13 :
    print(f'Your Age Is {age} and you are Child')
elif age >= 13 and age <= 19 : 
    print(f'Your Age Is {age} and you are Teenager')
elif age >= 20 and age <= 59 :
    print(f'Your Age Is {age} and you are Adult')
else :
    print(f'Your Age Is {age} and you are Senior')   
    