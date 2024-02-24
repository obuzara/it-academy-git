def geography(ask):
    a = {}
    for _ in range(2):
        s = input().split()
        country, cityes = s[0], s[1:]
        for city in cityes:
            a[city] = country
    for i in range(3):
        print(a[ask])


geography(ask="")
