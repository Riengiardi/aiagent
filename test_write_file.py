from functions.write_file import write_file

cases = [
    ("calculator", "lorem.txt", "wait, this isn't lorem ipsum"),
    ("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"),
    ("calculator", "/tmp/temp.txt", "this should not be allowed"),
]

for c in cases:
    print(f"--- Case: {c} ---\n")
    print(write_file(*c))