
number=int(input("Enter the Any number :"))

for i in range(1,11):
    if i==5:
        continue
    print(number,'*',i,"=",number*i)