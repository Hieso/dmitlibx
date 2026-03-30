import math
import operator
import toolz

def nod(numbers):
    return toolz.reduce(math.gcd, numbers)

def nok(numbers):
    return toolz.reduce(lambda a, b: abs(a * b) // math.gcd(a, b), numbers)

def average(scores):
    return sum(scores) / len(scores)