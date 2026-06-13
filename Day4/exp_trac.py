import json
from pydantic import BaseModel, ValidationError


class Expense(BaseModel):
    category: str
    amount: float


def add_expense(category: str, amount: float) -> None:
    try:
        expense = Expense(
            category=category,
            amount=amount
        )

        try:
            with open("expenses.json", "r") as file:
                expenses = json.load(file)
        except FileNotFoundError:
            expenses = []

        expenses.append(expense.model_dump())

        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=2)

        print("Expense Saved")

    except ValidationError as e:
        print("Validation Error")
        print(e)


add_expense("Food", 250)
add_expense("Travel", 500)
add_expense("Food", "abc")