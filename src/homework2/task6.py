n = list(input("Введите число n:"))
n1 = n
n = list(reversed(n))
if n == n1:
    print("урааа ура это палиндром!")
else:
    print("ураа ура это не палиндром!")

### ну если даже через список нельзя то разве что так

n = int(input("Введите число:"))
temp = n
rev = 0
while n > 0:
    dig = n % 10
    rev = rev * 10 + dig
    n = n // 10
if temp == rev:
    print("Это палиндром!")
else:
    print("Это не палиндром!")