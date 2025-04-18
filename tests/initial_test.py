from tmp_setup import *
setup()

from PyMath import *

a = Constant(5)
b = Constant(3.14)

assert(a > b)
assert(not (a == b))
assert(a != b)
assert(not (a < b))
assert(a >= b)
assert(not (a <= b))

c = Constant(5)

assert(not (a > c))
assert(a == c)
assert(not (a != c))
assert(not (a < c))
assert(a >= c)
assert(a <= c)

print("Passed")