username = "Zavyar"

def func():
    # username = "chai"
    print(username)

print(username)
func()


x = 99

# def func2(y):
    # x = 100
    # z = x + y
    # return z
# 
# print(func2(1))


# def func3():
    # global x
    # x = 12

def f1():
    x = 88
    def f2():
        print(x)
    f2()
f1()     


def chaicoder(num):
    def actual(y):
        return y ** num
    return actual

f = chaicoder(2)
g = chaicoder(3)

print(f(2))
print(g(3))


