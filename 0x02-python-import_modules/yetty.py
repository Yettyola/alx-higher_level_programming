#!/usr/bin/python3
# from test import *
# from sys import argv as q

# if len(q) != 4:
#     print("Usage: {} <a> <operator> <b>".format(q[0]))
#     exit(1)
# operators = "+-*/"
# operation = [add, sub, mul, div]
# if q[2] not in operators:

#     exit(1)
# a = int(q[1])
# b = int(q[3])

# print("{} {} {} = {}".format(a, q[2], b, operation[operators.index(q[2])](a, b)))





from test import *
from sys import argv as q

if len(q) != 4:
    print("Usage: {} <a> <operator> <b>".format(q[0]))
    exit(1)

opt = {"+":add, "-":sub, "*": mul, "/":div}
if (q[2]) not in opt:
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)
a = int(q[1])
b = int(q[3])

print("{} {} {} = {}".format(a, q[2], b, opt[q[2]](a, b)))
