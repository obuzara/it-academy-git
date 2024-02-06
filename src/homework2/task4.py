txt = input("Введите ваш текст: ")
print(f'Заглавных букв: {sum(map(str.isupper, txt))}, строчных: {sum(map(str.islower, txt))}')