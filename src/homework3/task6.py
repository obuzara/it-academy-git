def lis_cleanup():
    s = input().split()
    for i in reversed(range(len(s))):
        if s[i] == '0':
            s.append(s.pop(i))
    print(*s)


lis_cleanup()
