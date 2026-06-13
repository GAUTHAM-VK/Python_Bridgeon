class HTTPError(Exception):
    def __init__(self, status_code):
        self.status_code = status_code
        super().__init__(f"HTTP Error {status_code}")


def get_or_404(collection: dict, id: int) -> dict:
    if id in collection:
        return collection[id]
    raise HTTPError(404)


students = {
    1: {"name": "Alice"},
    2: {"name": "Bob"}
}

# Valid ID
print(get_or_404(students, 1))

# Invalid ID
try:
    print(get_or_404(students, 5))
except HTTPError as e:
    print(e)