#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments"""
    import sys

    count = len(sys.argv) - 1       # calculate commandline arguments
    if count == 1:
        print("1 arguments.")
    elif count == 0:
        print("0 argument:")
    else:
        print("{} arguments:".format(count))
    for i in range(count):      # iterate over the commandline arguments
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
