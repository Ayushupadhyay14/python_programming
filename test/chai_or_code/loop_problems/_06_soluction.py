"""Find the factorial in number :"""
number=int(input("Enter AnY number :To find factorial:"))
factorial=1

while number>0:
    factorial=factorial*number
    number=number-1
    if number==0:
        break
print(factorial)    