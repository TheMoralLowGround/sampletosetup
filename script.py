import math
import sys
from os import rename

test = "bigili"

print(sys.version)
print(sys.executable)


def greet(who_to_greet):
    return f"Hello {who_to_greet}"


print(greet("World"))
print(greet("Bigileee"))

name = input("Your Name?")
print(f"Hello {name}")
