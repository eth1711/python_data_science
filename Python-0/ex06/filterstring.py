import sys
import string
from ft_filter import ft_filter


def check_arg(text):
    """checks for punctuation and whether it is printable.
if all arguments valid, it returns True."""
    for x in text:
        if string.punctuation.find(x) != -1:
            return False
    if text.isprintable() is False:
        return False
    return True


def main():
    """check to make sure enough arguments. it runs and
prints the output of the filterstring"""
    assert len(sys.argv) == 3, "the arguments are bad"
    text = sys.argv[1]
    num = sys.argv[2]
    assert sys.argv[2].isdigit(), "arguments 2 not valid"
    assert check_arg(sys.argv[1]), "arguments 1 not valid"
    print(ft_filter(lambda word: len(word) > int(num), text.split()))


if __name__ == "__main__":
    main()
