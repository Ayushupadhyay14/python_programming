username="chaiaurcode"
def func():
    chaiaurcode="chsi"
    print(chaiaurcode)
# print(username)    

# func()
x=99

# def func2(y):
#     z=x+y
#     return z
# result=func2(1)
# print(result)


# def fun3():
#    global x
#    x=12
# fun3()
# print(x)    

def f1():
    x=22
    def f2():
        print(x)
    f2()
f1()       


def chaicoder(num):
    def actual(x):
        return x**num
    return actual
    

f=chaicoder(2)
g=chaicoder(3)
print(f(3))
print(g(3))
