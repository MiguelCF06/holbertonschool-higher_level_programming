#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    
    args = len(sys.argv)

    if (args-1 != 3):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    elif (sys.argv[2] == "+"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        res = add(a, b)
        print("{} + {} = {}".format(a, b, res))
    elif (sys.argv[2] == "-"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        res = sub(a, b)
        print("{} - {} = {}".format(a, b, res))
    elif (sys.argv[2] == "*"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        res = mul(a, b)
        print("{} * {} = {}".format(a, b, res))
    elif (sys.argv[2] == "/"):
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        res = div(a, b)
        print("{} / {} = {}".format(a, b, res))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
