txt = input("Введите ваш текст: ")
txt = txt.replace(" ","")
txt = "".join(set(txt))
print(txt)
