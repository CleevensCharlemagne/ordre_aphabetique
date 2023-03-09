
import sys

filename = sys.argv[1]

with open(filename, "r") as file:
    content = file.read().splitlines()
    content.sort()
    print(content)


