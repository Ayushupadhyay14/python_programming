

# class Person:
#   def __init__(mysillyobject, name, age):
#     mysillyobject.name = name
#     mysillyobject.age = age

#   def myfunc(abc):
#     print("Hello my name is "+ abc.name)

# p1 = Person("Amit_Upadhyay:", 76) 
# p2 = Person("Ayush_Upadhyay:", 43)
# p1.myfunc()
""" create a class name of the Car :"""

# class Car:
#   def __init__(self) -> None:
#      self.acc=False
#      self.brk=False
#      self.clutch=False
#      def start(self):
#        self.clutch=True
#        self.acc=True
#      print("Car is Started:..")
     
# c1=Car()
# print(c1.acc)
# print(c1.brk)
# print(c1.clutch)
class Student:
  def __init__(self,name):
     self.name=name
s1=Student("Ayush_upadhyay")
#del s1.name
print(s1.name)
#del s1.name