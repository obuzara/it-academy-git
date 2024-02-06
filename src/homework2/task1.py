
m = int(input("Введите стоимость товара в рублях "))
n = int(input("Введите стоимость товара в копейках "))
s = int(input("Введите количество единиц товара "))
cost = s * (100 * m + n)
price_rubles = cost // 100
price_cents = cost % 100
print("Стоимость товаров составляет ", price_rubles,  " рублей, ", price_cents, " копеек.")