from utils import greet,calculate_grade
name=input("Enter your name:")
print(greet(name))
marks=int(input("Enter  the mark:"))
print(f"grade:{calculate_grade(marks)}")
