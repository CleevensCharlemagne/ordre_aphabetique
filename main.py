
import sys

filename = sys.argv[1]
content = list()

with open(filename, "r") as file:
    content = file.read().splitlines()
    content.sort()

with open(filename, 'w') as file:
    for line in content:
        file.write(f"{line}\n")
        print(line)
