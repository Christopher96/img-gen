import random
import sys

with open("rand1", "w") as f:
    for i in range(0, sys.maxsize):
        f.write(str(random.randint(0,9)))
