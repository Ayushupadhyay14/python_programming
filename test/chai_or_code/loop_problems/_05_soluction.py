"""write down th code to find the single charter in given string """
input_str=str(input("Enter ANy charater values:"))

for char in input_str:
    print(char)
    if input_str.count(char)==1:
        print(f"NOn Repeated string"":char is :",char)
        break