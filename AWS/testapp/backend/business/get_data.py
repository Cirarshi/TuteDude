import os

def read_data() -> str:
    """Reads and returns content from data.txt inside the business folder."""
    filepath = os.path.join(os.path.dirname(__file__), "data.txt")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read()
    except FileNotFoundError:
        return "data.txt not found!"