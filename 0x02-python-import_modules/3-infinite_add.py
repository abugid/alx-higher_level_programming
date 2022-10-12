#!/usr/bin/python3
def main():
    import sys
    res = 0
    for i in range(1, len(sys.argv)):
        res += int(sys.argv[i])
    print(res)


if __name__ == "__main__":
    main()
