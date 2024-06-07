# import pyttsx3
# import os

# engine = pyttsx3.init()
# engine.say("Hello, World!")
# engine.runAndWait()

# os.system('echo Hello, World!')

x=int(input("Enter Any Year:"))
result="Leap Year" if x%400==0 else "Leap Year" if x%4==0 and x%100!=0 else "Non Leap Year"
print(result)  