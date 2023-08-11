#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argv_len = len(sys.argv)
    if argv_len != 4:
        print(f"Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    op = sys.argv[2]

    if op == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif op == "-":
        print("{} + {} = {}".format(a, b, sub(a, b)))
    elif op == "*":
        print("{} + {} = {}".format(a, b, mul(a, b)))
    elif op == "/":
        print("{} + {} = {}".format(a, b, div(a, b)))
    else:
        print(f"Unkown operator. Available operators: +, -, * and /")
        sys.exit(1)
