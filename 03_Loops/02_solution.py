num = int(input("Enter a Number: "))
sum_even = 0

for i in range(1, num + 1):
    if i % 2 == 0:
        sum_even += 1
print(f"Sum of even numbers: {sum_even}")