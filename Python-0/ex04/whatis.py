import sys

arg = sys.argv

if len(arg) != 2:
    print("AssertionError : more than one argument is provided ")
elif type(arg[1]) != int:
    print("AssertionError : argument is not an integer")
elif arg[1] % 2 == 0:
    print("I'm Even.")
elif arg[1] % 2 != 0:
    print("I'm Odd.")