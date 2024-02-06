side1 = float(input("Введите число side1:"))
side2 = float(input("Введите число side2:"))
side3 = float(input("Введите число side3:"))
sum_side1 = side1 + side2
sum_side2 = side1 + side3
sum_side3 = side2 + side3
if sum_side1 > side3 and sum_side2 > side2 and sum_side3 > side1:
    print("Это треугольник ураааа")
    p = (side1 + side2 + side3)/2
    s = (p * (p - side1) * (p - side2) * (p - side3)) ** 0.5
    print(f"Площадь треугольника равна: {s}")
else:
    print("это не треугольник урааа")
