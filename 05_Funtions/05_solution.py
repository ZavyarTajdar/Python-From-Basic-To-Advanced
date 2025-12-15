name = str(input("Enter Your Name : "))

def greet(Username):
    if Username:
        print(f"Hello! {name} , I hope you are doing great")
    else :
        print("hello User, I hope you are doing great")
greet(name)