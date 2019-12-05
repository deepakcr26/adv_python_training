class MyException(Exception):
    pass


d = {1: 1}
L = [0, 1, 2]
ctr = 1
while ctr != -1:
    try:
        ctr = int(input("Enter a number (-1 to exit): "))
        10/ctr
        if ctr == 2:
            ctr.int
        if ctr == 3:
            L[ctr]
        if ctr == 4:
            d[ctr]
        if ctr == 5:
            m[ctr]
        if ctr == 6:
            import ctr
        if ctr == 7:
            raise MyException
    except MyException as e:
        print("A Custom Exception is raised")
        print("Value of e: {} and its type is: {}".format(e, str(type(e))))
    except ValueError as e:
        print("That was not a valid number")
        print("Value of e: {} and its type is: {}".format(e, str(type(e))))
    except Exception as e:
        print("Default Exception handler, Enter -1 to exit")
        print("Value of e: {} and its type is: {}".format(e, str(type(e))))
    except:
        print("Final Exception")
    else:
        print("In else block")
    finally:
        print("In finally block")
