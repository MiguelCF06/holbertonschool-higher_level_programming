#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    args = len(sys.argv) - 1
    if args != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == "+":
            res = add(a, b)
            print("{} + {} = {}".format(a, b, res))
        elif sys.argv[2] == "-":
            res = sub(a, b)
            print("{} - {} = {}".format(a, b, res))
        elif sys.argv[2] == "*":
            res = mul(a, b)
            print("{} * {} = {}".format(a, b, res))
        elif sys.argv[2] == "/":
            res = div(a, b)
            print("{} / {} = {}".format(a, b, res))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            sys.exit(1)
