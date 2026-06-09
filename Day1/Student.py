class Student:

    def __init__(self, sid, name, marks):
        self.sid = sid
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent ID:", self.sid)
        print("Name:", self.name)
        print("Marks:", self.marks)

        if self.marks >= 90:
            print("Grade: A")
        elif self.marks >= 80:
            print("Grade: B")
        elif self.marks >= 70:
            print("Grade: C")
        elif self.marks >= 60:
            print("Grade: D")
        else:
            print("Grade: F")


students = []

for i in range(3):
    sid = int(input("Enter Student ID: "))
    name = input("Enter Student Name: ")
    marks = float(input("Enter Marks: "))

    s = Student(sid, name, marks)
    students.append(s)

for s in students:
    s.display()