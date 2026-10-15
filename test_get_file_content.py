from functions.get_file_content import get_file_content

test_cases = [
    ("calculator", "main.py"),
    ("calculator", "pkg/calculator.py"),
    ("calculator", "/bin/cat"),
    ("calculator", "pkg/does_not_exist.py"),
]

result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

for c in test_cases:
    print(f"--- Case: {c} ---\n")
    print(get_file_content(*c))