#!/usr/bin/python3
from sys import argv

args = argv[1:]
sum = 0
for arg in args:
    sum += int(arg)
print(f"{sum}")

if __name__ != "__main__":
    main()
