# (chr(ord('a')+i)) сделает мне перечислялку по алфавиту
# for i in range (4):
#     for j in range (i):
#         a= (chr(ord('a')+j))
#         b= (chr(ord('a')+i))
#         print (a+b)
def hehe_i_did_it():
    ab = [(chr(ord('a') + j)) + (chr(ord('a') + i)) for i in range(4) for j in range(i)]
    return ab

# print(hehe_i_did_it())

# print (hehe_i_did_it()[::2])
def lis2 (num):
    your_ad_could_be_here =[str(i) + 'a' for i in range(num)]
    return (your_ad_could_be_here[1:])

# print (lis2(num=5))
a=lis2(num=5)
print(a.pop(1)) #одной строкой вызвали по индексу и стерли, можно прописать сразу с функции? и оно по идее работает??
b=a[:]
print(b) # подзастряла на моменте, напрямую с функции скопировать с удаленным
        #элементом не получилось, пришлось использовать костыль с доп.переменной, пахнет плохо

