#!/usr/bin/python3
import sys
argv = sys.argv


def main():
    str_end = "." if len(argv) == 1 else ":"
    print("{} arguments{}".format(len(argv) - 1, str_end))
    for i in range(1, len(argv)):
        print("{} : {}".format(i, argv[i]))


if __name__ == "__main__":
    main()
