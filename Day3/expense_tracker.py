import json
from typing import List, Dict, Any


def load_expenses() -> List[Dict[str, Any]]:
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def save_expenses(expenses: List[Dict[str, Any]]) -> None:
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=2)


def add_expense(category: str, amount: float) -> None:
    expenses: List[Dict[str, Any]] = load_expenses()

    expense: Dict[str, Any] = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("Expense added successfully.")


def get_summary() -> Dict[str, float]:
    expenses: List[Dict[str, Any]] = load_expenses()

    summary: Dict[str, float] = {}

    for expense in expenses:
        category: str = expense["category"]
        amount: float = expense["amount"]

        summary[category] = summary.get(category, 0) + amount

    return summary


def view_all() -> None:
    expenses: List[Dict[str, Any]] = load_expenses()

    for expense in expenses:
        print(
            f"Category: {expense['category']} | Amount: ₹{expense['amount']}"
        )


def read_logs() -> None:
    counts: Dict[str, int] = {}

    try:
        with open("log.txt", "r") as file:
            for line in file:
                parts: list[str] = line.split("|")

                if len(parts) >= 2:
                    func_name: str = parts[1].strip()

                    counts[func_name] = counts.get(func_name, 0) + 1

        for func, count in counts.items():
            print(f"{func}: {count}")

    except FileNotFoundError:
        print("No log file found.")