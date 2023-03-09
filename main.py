
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    content = file.read().splitlines()
    content.sort()
    print(content)

with open('your_file.txt', 'w') as file:
    for line in content:
        file.write(f"{line}\n")
    print(content)
