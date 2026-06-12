def calculate_grade(marks: int) -> str:
    if marks >= 90:
        return "A"
    elif marks >= 80:
        return "B"
    elif marks >= 70:
        return "C"
    elif marks >= 60:
        return "D"
    else:
        return "F"


def display_result(name: str, marks: int) -> None:
    grade: str = calculate_grade(marks)
    print(f"Student: {name}")
    print(f"Marks: {marks}")
    print(f"Grade: {grade}")


def main() -> None:
    name: str = input("Enter student name: ")
    marks: int = int(input("Enter marks: "))
    display_result(name, marks)


main()