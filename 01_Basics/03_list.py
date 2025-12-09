tea_varities = ["Green Tea", "Black Tea", "Oolong Tea", "White Tea"]

print(tea_varities[1:3])

tea_varities[1] = "Herbal Tea"

print(tea_varities)

tea_varities.append("Masala Tea")
print(tea_varities)

tea_varities.remove("Oolong Tea")
print(tea_varities)

tea_varities.sort()
print(tea_varities)

for tea in tea_varities:
    print("I love " + tea)


if "Green Tea" in tea_varities:
    print("Green Tea is available!")

tea_varities.pop()
tea_varities.pop(1)
tea_varities.insert(2, "Chamomile Tea")
print(tea_varities)

tea_varities_copy = tea_varities.copy()
print(tea_varities_copy)

tea_varities.clear()
print(tea_varities)

squares = [x**2 for x in range(10)]
print(squares)

cube = [y**3 for y in range(10)]
print(cube)