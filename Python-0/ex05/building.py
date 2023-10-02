import sys
import string


def main():
    """Main function that takes one single string argument
    and displays the sum of the certain types of characters
    in the given string. Only one argument can be taken.
    If no argument is given, input is asked from the user.
    """
    arg = sys.argv
    assert len(arg) <= 2, "more than one argument is provided"

    if len(arg) == 1:
        str = input("What is the text to count?\n")
    else:
        str = arg[1]
    upper, lower, punc, spaces, digits, num = 0, 0, 0, 0, 0, 0
    for i in str:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i in string.punctuation:
            punc += 1
        elif i.isspace():
            spaces += 1
        elif i.isdigit():
            digits += 1
        num += 1
    print(f"The text contains {num} characters")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punc} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
