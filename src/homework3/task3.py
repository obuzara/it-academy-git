def tuple_practice(num):
    a = [(chr(ord('a') + i)) for i in range(num)]
    b = tuple(a)
    return b


# print(tuple_practice(3))

def tuple_practice_2(num):
    a1 = ((chr(ord('a') + i)) for i in range(num))
    b1 = list(a1)
    return b1


# print(tuple_practice_2(3))
a, b, c = 'a', 2, 'python'  # присвоение одной строкой :)
# print(a,b,c)

# могу еще вот так, двумя, но в тапл
tuple_one = 'a', 2, 'python'
a, b, c = tuple_one
# print(tuple_one)

tuple_two = ([1, 2, 3],)


def tuple_iteration():
    for i in range(len(tuple_two)):
        for j in range(len(tuple_two[i])):
            print(tuple_two[i][j], end=' ')
# tuple_iteration()
