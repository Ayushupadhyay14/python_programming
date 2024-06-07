""" find the prime number in given data"""

# number=int(input("Enter ANy nuber :"))

# if number%2==0:
#     print("number is not prime")
# else:
#     print("number is prime:")  

number=int(input("Enter ANy number for Given by user:"))

is_prime=True

if number>1:
    for i in range(2,number):
        if (number%i)==0:
            is_prime=False
            break
print(is_prime)        
            