import math
from multiprocessing.sharedctypes import Value

try:

    print(eval(math.sqrt(-1)))
except SyntaxError:
    print("b")
except ValueError:
    print("a")
