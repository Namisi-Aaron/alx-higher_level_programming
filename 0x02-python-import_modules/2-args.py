#!/usr/bin/python3
from sys import argv

num_of_arguments = len(argv) - 1
if num_of_arguments == 0:
    print(f"{num_of_arguments} arguments.")
elif num_of_arguments > 1:
    print(f"{num_of_arguments} arguments:")
else:
    print(f"{num_of_arguments} argument:")
for i in range(num_of_arguments):
    print(f"{i + 1}: {argv[i + 1]}")
