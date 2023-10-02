import sys

arg = sys.argv

assert len(arg) <= 2, "more than one argument is provided"

assert arg[1].isnumeric(), "argument is not an interger"

num = int(arg[1])
if num % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
