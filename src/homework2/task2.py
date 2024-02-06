txt = input("Введите ваш текст: ")
txt = txt.replace(",""")
print(max(txt.split(), key=len))
