def squares(n):
    return n*n


l = [1, 2, 3, 4, 5]

new_list = map(squares, l)
print(list(new_list))


def lt100(n):
    if n < 100:
        return True
    return False


l = [1, 2, 10, 20, 30, 105, 125, 95, 80, 76]
l1 = filter(lt100, l)
print(list(l1))
