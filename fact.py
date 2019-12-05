from sys import path


def fact(n):
    if 0 == n or 1 == n:
        return 1
    return n*fact(n-1)


if __name__ == '__main__':
    print(fact(5), __name__)
    print("sys.path: {}".format(path))
else:
    print(__name__)
