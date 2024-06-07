
""" """
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        
    def get_avg(self):
        total_marks = sum(self.marks)
        average = total_marks / len(self.marks)
        print("Hello", self.name + ",", "your average score is:", average)


# Example usage:
S1 = Student("Tony Stark", [99,98,97])
S1.get_avg()
S1.name="Ayush upadhyay"
S1.get_avg()
