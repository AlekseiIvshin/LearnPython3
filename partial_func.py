from functools import partial

def multiply(x, y):
  return x * y;

dbl = partial(multiply, 2)
print(dbl(4))
print(dbl)

def func(u,v,w,x):
    return u*4 + v*3 + w*2 + x

part = partial(func, 5, 6, 7)
print(part(8))
