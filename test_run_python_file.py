from functions.run_python_file import run_python_file

cases = [
    ("calculator", "main.py"),
    ("calculator", "main.py", ["3 + 5"]),
    ("calculator", "tests.py"),
    ("calculator", "../main.py"),
    ("calculator", "nonexistent.py"),
    ("calculator", "lorem.txt"),
]

for c in cases:
    print(f"--- Case: {c} ---\n")
    print(run_python_file(*c) + "\n")