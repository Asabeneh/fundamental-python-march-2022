# A function that returns other function
# A function that takes other function as a parameter

from cmath import sqrt
from tkinter import N


def do_math(n):
  def add_ten():
    return n + 10
  return add_ten

print(do_math(10)())

print(do_math(100)())

def make_square(n):
  return n ** 2

def make_cube(f, n):
  return f(n) * n

print(make_cube(make_square, 2))
print(make_cube(make_square, 3))
