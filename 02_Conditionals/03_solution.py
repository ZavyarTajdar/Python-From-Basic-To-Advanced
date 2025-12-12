score = int(input("Enter Your Score : "))

if score >= 90 and score <= 100 : 
    print(f"Your Score Is {score} and Your Percentage Grade is A")
elif score >= 80 and score <= 89 : 
    print(f"Your Score Is {score} and Your Percentage Grade is B")
elif score >= 70 and score <= 79 : 
    print(f"Your Score Is {score} and Your Percentage Grade is C")
elif score >= 60 and score <= 69 : 
    print(f"Your Score Is {score} and Your Percentage Grade is D")
elif score <= 59 : 
    print(f"Your Score Is {score} and Your Percentage Grade is F Means You Are Fail")
else :
    print("Invalid Score")