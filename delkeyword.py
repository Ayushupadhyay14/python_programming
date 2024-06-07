# """used to delete object properties or object itself:"""
# class Student:
#     def __init__(self,name):
#         self.name=name
# s1=Student("Ayush")
# print(s1.name)
# del s1.name
# print(s1)
class Data:
    def __init__(self,name,dep,marks):
        self.name=name
        self.dep=dep
        self.marks=marks
    def welcome(self):
            print("Welcome to Apna college:")
        
D1=Data("Ayush","BCA+MCA",98)
print("Name of the student is :=> ",D1.name)
print("Name of a Depetrment of :=> ",D1.dep)
print("Marks oF the student:=> ",D1.marks)
