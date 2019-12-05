a, b, c, d = 10, 20, 30, 40


def FuncA():
    a, b, c = 100, 200, 300
    print("In FuncA", a, b, c, d)

    def FuncB():
        a, b = 1000, 2000
        print("In FuncB", a, b, c, d)

        def FuncC():
            a = 10000
            print("In FuncC", a, b, c, d)
        FuncC()
    FuncB()


FuncA()
print("In __main__", a, b, c, d)
