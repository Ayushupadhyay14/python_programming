class Student:
    student_count = 0  # Class attribute to keep track of the number of students

    def __init__(self, name,marks):
        self.name = name # Appending unique identifier
        #Student.student_count += 1
        self.marks = marks # Incrementing the student count
        print("Adding new student to the database:", self.name)


s1 = Student("Amit",56)
print(s1.name,s1.marks)
s2 = Student("Ankit",86)
print(s2.name,s2.marks)
