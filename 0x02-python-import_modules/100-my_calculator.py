#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    if (len(sys.argv) != 4):
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)
    from calculator_1 import add, sub, mul, div
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    symbol = sys.argv[2]
    operators = {
        '+': add(a, b),
        '-': sub(a, b),
        '*': mul(a, b),
        '/': div(a, b)
    }
    try:
        print("{:d} {} {:d} = {:d}".format(a, symbol, b, operators[symbol]))
    except KeyError:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
