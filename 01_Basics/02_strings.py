chai = "Masala Chai"
print(chai)
# print(type(chai))

slice_chai = chai[7: 11]
slice_masala = chai[0:6]
# print(slice_chai)
# print(slice_masala)

num_list = "0123456789"

# slice_num = num_list[0:9:4]
# slice_num = num_list[0:7:3]
# slice_num = num_list[::-1]
slice_num = num_list[9 : -1]
# print(slice_num)


# print(chai.lower())
# print(chai.upper())

chai2 = " hello chai    "

# print(chai2.strip())

# print(chai.replace("Chai", "Coffee"))

tea = "cold, hot, cold, hot, cold, hot, ice, molten"

# print(tea.split(","))
# print(tea.find("h"))

# print(tea.count("hot"))

chai_type = "masala"
quantity = 2

order = f"I ordered {quantity} cups of {chai_type} chai"
# print(order)

chai_variety = ["Lemon", "Masala", "Ginger"]
# print(", ".join(chai_variety))

# print(len(chai))

# for letter in chai :
#     print(letter)

statement = "He said, \'Masala Chai Is Awesome\' "
# print(statement)

chai3 = r"Masala\nChai"
print(chai3)