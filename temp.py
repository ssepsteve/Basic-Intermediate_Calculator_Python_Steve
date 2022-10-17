import math

ln = lambda i: math.log(i,math.e)
euler = math.e
print(eval("l(e)",{},{"l":ln,"e":euler}))