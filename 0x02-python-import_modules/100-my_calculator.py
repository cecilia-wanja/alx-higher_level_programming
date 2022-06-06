#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, mul, div
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if args[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(args[1])
    b = int(args[3])
    ops = args[2]
    if ops == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, add(a, b)))
    elif ops == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, sub(a, b)))
    elif ops == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, mul(a, b)))
    elif ops == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, ops, b, div(a, b)))
