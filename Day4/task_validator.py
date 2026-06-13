from pydantic import BaseModel, ValidationError


class TaskModel(BaseModel):
    title: str
    priority: str = "low"
    completed: bool = False


# Correct data
task = TaskModel(
    title="Complete Assignment",
    priority="high",
    completed=True
)

print(task)

# Wrong data
try:
    task2 = TaskModel(
        title=123,
        priority=100,
        completed="abc"
    )
except ValidationError as e:
    print("\nValidation Error:")
    print(e)